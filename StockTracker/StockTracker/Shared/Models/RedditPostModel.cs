using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace StockTracker.Shared.Models
{
    public class RedditPostModel
    {
        [JsonPropertyName("stock")]
        public string stock { get; set; }
        [JsonPropertyName("postID")]
        public string postID { get; set; }
        [JsonPropertyName("postURL")]
        public string postURL { get; set; }
        [JsonPropertyName("ups")]
        public int ups { get; set; }
        [JsonPropertyName("downs")]
        public int downs { get; set; }
        [JsonPropertyName("numComments")]
        public int numComments { get; set; }
        [JsonPropertyName("LastModified")]
        public DateTime LastModified { get; set; } = DateTime.UtcNow;
    }
}
