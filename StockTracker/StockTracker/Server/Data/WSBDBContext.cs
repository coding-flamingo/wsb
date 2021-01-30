using Microsoft.Azure.Services.AppAuthentication;
using Microsoft.EntityFrameworkCore;
using StockTracker.Shared.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace StockTracker.Server.Data
{
    public class WSBDBContext : DbContext
    {
        public virtual DbSet<RedditPostModel> Posts { get; set; }

        public WSBDBContext(DbContextOptions<WSBDBContext> options) : base(options)
        {
            var con = (Microsoft.Data.SqlClient.SqlConnection)Database.GetDbConnection();
            if (con.ConnectionString.Contains("(localdb)", StringComparison.OrdinalIgnoreCase))
            {
                return; // no MSI needed when using local db
            }

            con.AccessToken = new AzureServiceTokenProvider()
                .GetAccessTokenAsync("https://database.windows.net/")
                .Result;
        }
    }
}
