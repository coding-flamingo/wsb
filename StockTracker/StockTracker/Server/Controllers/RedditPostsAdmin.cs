using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using StockTracker.Server.Managers;
using StockTracker.Shared.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;

namespace StockTracker.Server.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class RedditPostsAdmin : ControllerBase
    {
        private readonly PostsManager _postsManager;
        private readonly ILogger _logger;
        public RedditPostsAdmin(PostsManager postsManager, ILogger<RedditPostsAdmin> logger)
        {
            _postsManager = postsManager;
            _logger = logger;
        }
        [HttpPost]
        public async Task<string> PostReditPosts(List<RedditPostModel> postsList)
        {
            string signature = Request.Headers["Flamingo-Signature"];
            if (string.IsNullOrWhiteSpace(signature) || !signature.Equals(""))
            {
                return "you naughty boy stop trying to add stuff";
            }
            if (!_postsManager.IsPostListValid(postsList))
            {
                return "Invalid posts found";
            }

            try
            {
                return await _postsManager.AddPostsAsync(postsList);
            }
            catch (Exception ex)
            {
                _logger.LogError("error adding posts",ex);
                return ex.Message;
            }
        }
    }
}
