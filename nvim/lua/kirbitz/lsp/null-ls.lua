local null_ls_status_ok, null_ls = pcall(require, "null-ls")
if not null_ls_status_ok then
	vim.notify("Null LS failed to load!", vim.log.levels.ERROR, { title = "Package Failure" })
	return
end

local mason_null_ls_status_ok, mason_ls = pcall(require, "mason-null-ls")
if not mason_null_ls_status_ok then
	vim.notify("Mason Null LS failed to load!", vim.log.levels.ERROR, { title = "Package Failure" })
	return
end

local formatting = null_ls.builtins.formatting

local diagnostics = null_ls.builtins.diagnostics

local augroup = vim.api.nvim_create_augroup("LspFormatting", {})

null_ls.setup({
	debug = false,
	sources = {
		formatting.prettier.with({
			extra_args = { "--no-semi", "--single-quote", "--jsx-single-quote" },
		}),
		formatting.black.with({ extra_args = { "--fast" } }),
		formatting.stylua,
		formatting.clang_format,
		diagnostics.flake8,
		diagnostics.eslint_d,
	},
	-- you can reuse a shared lspconfig on_attach callback here
	on_attach = function(client, bufnr)
		if client.supports_method("textDocument/formatting") then
			vim.api.nvim_clear_autocmds({ group = augroup, buffer = bufnr })
			vim.api.nvim_create_autocmd("BufWritePre", {
				group = augroup,
				buffer = bufnr,
				callback = function()
					-- on 0.8, you should use vim.lsp.buf.format({ bufnr = bufnr }) instead
					vim.lsp.buf.format({ async = false })
				end,
			})
		end
	end,
})

mason_ls.setup({
	ensure_installed = { "prettier", "black", "stylua", "flake8", "cspell", "eslint" },
	automatic_installation = true,
})
