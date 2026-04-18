// Data/AppDbContext.cs
using Microsoft.EntityFrameworkCore;
using SRWS_API.Models;

namespace SRWS_API.Data;

public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }

    public DbSet<ScanHistory>   ScanHistories   => Set<ScanHistory>();
    public DbSet<WasteCategory> WasteCategories => Set<WasteCategory>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {

        modelBuilder.Entity<WasteCategory>().ToTable("waste_categories");
        modelBuilder.Entity<ScanHistory>().ToTable("scan_history");


        modelBuilder.Entity<ScanHistory>(e =>
        {
            e.HasKey(s => s.Id);
            e.Property(s => s.ConfidenceScore).HasColumnType("decimal(5,4)");
        });

        // Seed: 5 Kategori
        modelBuilder.Entity<WasteCategory>().HasData(
            new WasteCategory { Id = 1, Name = "Plastic",           ColorHex = "#FFC107", IconName = "local_drink",  RecyclingBinColor = "Yellow bin" },
            new WasteCategory { Id = 2, Name = "Paper & Cardboard", ColorHex = "#2196F3", IconName = "description",  RecyclingBinColor = "Blue bin"   },
            new WasteCategory { Id = 3, Name = "Metal",             ColorHex = "#9E9E9E", IconName = "inbox",        RecyclingBinColor = "Grey bin"   },
            new WasteCategory { Id = 4, Name = "Battery",           ColorHex = "#F44336", IconName = "battery_alert",RecyclingBinColor = "Red bin"    },
            new WasteCategory { Id = 5, Name = "Glass",             ColorHex = "#00BCD4", IconName = "wine_bar",     RecyclingBinColor = "Blue bin"   }
        );
    }
}