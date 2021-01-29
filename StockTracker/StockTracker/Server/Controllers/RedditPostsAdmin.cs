using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
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
        [HttpPost]
        public string PostReditPosts(RedditPostModel [] postsArray)
        {
            return "hi";
        }
    }
}
