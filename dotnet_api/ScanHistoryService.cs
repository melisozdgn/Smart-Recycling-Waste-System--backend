// Services/IScanHistoryService.cs + ScanHistoryService.cs
using Microsoft.EntityFrameworkCore;
using SRWS_API.Data;
using SRWS_API.Models;

namespace SRWS_API.Services;

public record GuestScanRequest(
    string  CategoryName,
    decimal ConfidenceScore,
    string? AiDescription,
    string? DeviceId
);

public record ScanHistoryResponse(
    Guid     Id,
    string   CategoryName,
    decimal  ConfidenceScore,
    string?  AiDescription,
    DateTime ScannedAt
);

public interface IScanHistoryService
{
    Task<ScanHistoryResponse>       AddScanAsync(GuestScanRequest request);
    Task<List<ScanHistoryResponse>> GetHistoryAsync(string? deviceId, int page, int pageSize);
}

public class ScanHistoryService : IScanHistoryService
{
    private readonly AppDbContext _db;
    public ScanHistoryService(AppDbContext db) => _db = db;

    public async Task<ScanHistoryResponse> AddScanAsync(GuestScanRequest request)
    {
        var scan = new ScanHistory
        {
            DeviceId        = request.DeviceId,
            CategoryName    = request.CategoryName,
            ConfidenceScore = request.ConfidenceScore,
            AiDescription   = request.AiDescription,
        };
        _db.ScanHistories.Add(scan);
        await _db.SaveChangesAsync();

        return new ScanHistoryResponse(
            scan.Id, scan.CategoryName, scan.ConfidenceScore,
            scan.AiDescription, scan.ScannedAt);
    }

    public async Task<List<ScanHistoryResponse>> GetHistoryAsync(
        string? deviceId, int page, int pageSize)
    {
        var query = _db.ScanHistories.AsQueryable();

        if (!string.IsNullOrEmpty(deviceId))
            query = query.Where(s => s.DeviceId == deviceId);

        return await query
            .OrderByDescending(s => s.ScannedAt)
            .Skip((page - 1) * pageSize)
            .Take(pageSize)
            .Select(s => new ScanHistoryResponse(
                s.Id, s.CategoryName, s.ConfidenceScore,
                s.AiDescription, s.ScannedAt))
            .ToListAsync();
    }
}
