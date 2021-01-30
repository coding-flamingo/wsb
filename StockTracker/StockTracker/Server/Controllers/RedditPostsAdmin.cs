using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using StockTracker.Server.Managers;
using StockTracker.Shared.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace StockTracker.Server.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class RedditPostsAdmin : ControllerBase
    {
        private readonly PostsManager _postsManager;
        public RedditPostsAdmin(PostsManager postsManager)
        {
            _postsManager = postsManager;
        }
        [HttpPost]
        public async Task<string> PostReditPosts(List<RedditPostModel> postsList)
        {
            string signature = Request.Headers["Flamingo-Signature"];
            if (!_postsManager.IsPostListValid(postsList))
            {
                return "Invalid posts found";
            }
            return await _postsManager.AddPostsAsync(postsList);
        }
    }
}
