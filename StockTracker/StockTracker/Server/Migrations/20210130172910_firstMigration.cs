using Microsoft.EntityFrameworkCore.Migrations;

namespace StockTracker.Server.Migrations
{
    public partial class firstMigration : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Posts",
                columns: table => new
                {
                    postID = table.Column<string>(type: "nvarchar(450)", nullable: false),
                    stock = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    postURL = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    ups = table.Column<int>(type: "int", nullable: false),
                    downs = table.Column<int>(type: "int", nullable: false),
                    numComments = table.Column<int>(type: "int", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Posts", x => x.postID);
                });
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "Posts");
        }
    }
}
