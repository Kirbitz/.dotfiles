local status_ok, _ = pcall(require, "lspconfig")
if not status_ok then
	vim.notify("LSPConfig failed to load!", vim.log.levels.ERROR, { title = "Package Failure" })
	return
end

require("kirbitz.lsp.handlers").setup()
require("kirbitz.lsp.lsp-installer")
require("kirbitz.lsp.null-ls")
require("kirbitz.lsp.dap")
