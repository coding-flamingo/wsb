using Microsoft.Extensions.Logging;
using StockTracker.Server.Data;
using StockTracker.Shared.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace StockTracker.Server.Managers
{
    public class PostsManager
    {
        private readonly ILogger _logger;
        private readonly WSBDBContext _dbContext;
        public PostsManager(WSBDBContext wSBDB, ILogger<PostsManager> logger)
        {
            _logger = logger;
            _dbContext = wSBDB;
        }

        public bool IsPostListValid(List<RedditPostModel> postsList)
        {
            if (postsList == null)
            {
                return false;
            }
            foreach (RedditPostModel post in postsList)
            {
                if (post == null)
                {
                    return false;
                }
                if (post.ups < 0 || post.downs < 0)
                {
                    return false;
                }
            }
            return true;
        }

        public async Task<string> AddPostsAsync(List<RedditPostModel> postsList)
        {
            if(!IsPostListValid(postsList))
            {
                return "Invalid posts found";
            }
            IEnumerable<RedditPostModel> existingPosts =  _dbContext.Posts.Where(i =>
                postsList.Select(x => x.postID).Contains(i.postID));
            RedditPostModel existingPost;
            foreach(RedditPostModel post in postsList)
            {
                existingPost = existingPosts.FirstOrDefault(x => x.postID == post.postID 
                && x.stock == post.stock);
                if(existingPost == null)
                {
                    _dbContext.Posts.Add(post);
                }
                else
                {
                    existingPost.ups = post.ups;
                    existingPost.downs = post.downs;
                    existingPost.numComments = post.numComments;
                }
            }
            try
            {
                await _dbContext.SaveChangesAsync();
            }
            catch(Exception ex)
            {
                _logger.LogError("Error saving changes  in DB", ex);
                return "Error saving changes in DB";
            }
            return "success";
        }
    }
}
