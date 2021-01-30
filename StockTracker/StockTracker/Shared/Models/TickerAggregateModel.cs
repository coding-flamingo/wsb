using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace StockTracker.Shared.Models
{
    public class TickerAggregateModel
    {
        [JsonPropertyName("StockTicker")]
        public string StockTicker { get; set; }
        [JsonPropertyName("UpVotes")]
        public int UpVotes { get; set; }
        [JsonPropertyName("DownVotes")]
        public int DownVotes { get; set; }
        [JsonPropertyName("Comments")]
        public int Comments { get; set; }
    }
}
