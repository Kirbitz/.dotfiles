local status_ok, tint = pcall(require, "tint")
if not status_ok then
  vim.notify("Tint Nvim failed to load!", vim.log.levels.ERROR, { title = "Package Failure" })
  return
end

tint.setup({
  tint = -55,
  saturation = 0.6,
  window_ignore_function = function(winid)
    local bufid = vim.api.nvim_win_get_buf(winid)
    local buftype = vim.api.nvim_buf_get_option(bufid, "buftype")
    local floating = vim.api.nvim_win_get_config(winid).relative ~= ""

    return buftype == "terminal" or floating
  end,
})
