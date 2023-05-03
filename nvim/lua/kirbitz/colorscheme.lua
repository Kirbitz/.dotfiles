local colorscheme = "catppuccin-mocha"

local status_ok, _ = pcall(vim.cmd, "colorscheme " .. colorscheme)
if not status_ok then
  vim.notify("colorscheme " .. colorscheme .. " not found!", vim.log.levels.WARN, { title = "Colorscheme Not Found" })
  return
end
