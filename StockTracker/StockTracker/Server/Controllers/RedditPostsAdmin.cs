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
        public async Task PostReditPosts(List<RedditPostModel> postsList)
        {
            string signature = Request.Headers["Flamingo-Signature"];
            //get all the posts where postsList.Contains(i.postID)
            //if it exists update values if it doesnt, add
            //save changes Async
            return;
        }
    }
}
