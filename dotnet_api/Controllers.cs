using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using SRWS_API.Data;
using SRWS_API.Services;
// using SRWS_API.Models;

namespace SRWS_API.Controllers;

[ApiController]
[Route("api/scan")]
public class ScanController : ControllerBase
{
    private readonly IScanHistoryService _scanService;
    public ScanController(IScanHistoryService scanService) => _scanService = scanService;

    /// POST /api/scan/history
    [HttpPost("history")]
    public async Task<IActionResult> AddScan([FromBody] GuestScanRequest request)
    {
        var result = await _scanService.AddScanAsync(request);
        return Ok(result);
    }

    /// GET /api/scan/history?deviceId=xxx&page=1

    [HttpGet("history")]
    public async Task<IActionResult> GetHistory(
        [FromQuery] string? deviceId,
        [FromQuery] int page     = 1,
        [FromQuery] int pageSize = 20)
    {
        var result = await _scanService.GetHistoryAsync(deviceId, page, pageSize);
        return Ok(result);
    }
}

[ApiController]
[Route("api/categories")]
public class CategoriesController : ControllerBase
{
    private readonly AppDbContext _db;
    public CategoriesController(AppDbContext db) => _db = db;

    /// GET /api/categories

    [HttpGet]
    public async Task<IActionResult> GetAll()
    {
        var categories = await _db.WasteCategories
            .Select(c => new {
                c.Id, c.Name, c.ColorHex,
                c.IconName, c.RecyclingBinColor, c.Description
            })
            .ToListAsync();
        return Ok(categories);
    }
}