// Models.cs
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace SRWS_API.Models;

public class ScanHistory
{
    [Key]
    [Column("id")]
    public Guid Id { get; set; } = Guid.NewGuid();

    [MaxLength(255)]
    [Column("device_id")]
    public string? DeviceId { get; set; }      // Anonim cihaz kimliği

    [Required, MaxLength(100)]
    [Column("category_name")]
    public string CategoryName { get; set; } = string.Empty;

    [Required]
    [Column("confidence_score", TypeName = "decimal(5,4)")]
    public decimal ConfidenceScore { get; set; }

    [Column("ai_description")]
    public string? AiDescription { get; set; }

    [Column("scanned_at")]
    public DateTime ScannedAt { get; set; } = DateTime.UtcNow;
}

public class WasteCategory
{
    [Key]
    [Column("id")]
    public int Id { get; set; }

    [Required, MaxLength(100)]
    [Column("name")]
    public string Name { get; set; } = string.Empty;

    [MaxLength(7)]
    [Column("color_hex")]
    public string ColorHex { get; set; } = "#4CAF50";

    [Column("icon_name")]
    public string IconName { get; set; } = "recycling";

    [Column("recycling_bin_color")]
    public string? RecyclingBinColor { get; set; }

    [Column("description")]
    public string? Description { get; set; }

    [Column("created_at")]
    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
}