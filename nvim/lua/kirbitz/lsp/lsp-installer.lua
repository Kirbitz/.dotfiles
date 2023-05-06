local mason_status_ok, mason = pcall(require, "mason")
if not mason_status_ok then
	vim.notify("Mason failed to load!", vim.log.levels.ERROR, { title = "Package Failure" })
	return
end

local mason_lsp_status_ok, mason_lsp = pcall(require, "mason-lspconfig")
if not mason_lsp_status_ok then
	vim.notify("Mason LSPConfig failed to load!", vim.log.levels.ERROR, { title = "Package Failure" })
	return
end

mason.setup()
mason_lsp.setup()

local lsp_status_ok, lspconfig = pcall(require, "lspconfig")
if not lsp_status_ok then
	vim.notify("LSPConfig failed to load!", vim.log.levels.ERROR, { title = "Package Failure" })
	return
end

-- Register a handler that will be called for all installer servers.
-- Alternatively, you may also register handlers on specific server instances instead (see example below).
mason_lsp.setup_handlers({
	function(ls)
		local config = require("kirbitz.lsp.handlers")
		local ok, override = pcall(require, "kirbitz.lsp.settings." .. ls)
		if ok then
			config = vim.tbl_deep_extend("force", config, override)
		end
		lspconfig[ls].setup(config)
	end,
})
