local status_ok, configs = pcall(require, "nvim-treesitter.configs")
if not status_ok then
	vim.notify("Nvim Treesitter failed to load!", vim.log.levels.ERROR, { title = "Package Failure" })
	return
end

configs.setup({
	ensure_installed = {
		"c",
		"lua",
		"vim",
		"vimdoc",
		"query",
		"rust",
		"python",
		"bash",
		"javascript",
		"elixir",
		"go",
		"dart",
		"gitignore",
		"julia",
		"ocaml",
	},
	sync_install = false,
	ignore_install = { "" },
	autopairs = {
		enable = true,
	},
	highlight = {
		enable = true,
		disable = { "" },
		additional_vim_regex_highlighting = true,
	},
	indent = { enable = true, disable = { "yaml" } },
	context_commentstring = {
		enable = true,
		enable_autocmd = false,
	},
	rainbow = {
		enable = true,
		extended_mode = true,
		max_file_lines = nil,
	},
})
