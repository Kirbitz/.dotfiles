local status_ok, notify = pcall(require, "notify")
if not status_ok then
  vim.notify("Notify failed to load!", vim.log.levels.ERROR, { title = "Package Failure" })
  return
end

vim.notify = notify
