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
    public class ReadPostsController : ControllerBase
    {
        private readonly PostsManager _postsManager;
        public ReadPostsController(PostsManager postsManager)
        {
            _postsManager = postsManager;
        }

        [HttpGet("GetPupularStocks")]
        public List<TickerAggregateModel> GetPupularStocks()
        {
            return _postsManager.GetPopularStocks();
        }
        [HttpGet("GetStockPosts")]

        public IEnumerable<RedditPostModel> GetStockPosts(string stock)
        {
            if(!_postsManager.StockTickerIsValid(stock.Trim()))
            {
                return new List<RedditPostModel>();
            }
            return _postsManager.GetStockPosts(stock.ToUpper().Trim());
        }
    }
}
