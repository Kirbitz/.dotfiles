local indent_status_ok, indent_blankline = pcall(require, "indent_blankline")
if not indent_status_ok then
	vim.notify("Indent Blankline failed to load!", vim.log.levels.ERROR, { title = "Package Failure" })
	return
end

vim.g.indent_blankline_filetype_exclude = { "dashboard", "lspinfo", "packer", "checkhealth", "help", "man" }

vim.cmd([[highlight IndentBlanklineIndent1 guifg=#4F000B gui=nocombine]])
vim.cmd([[highlight IndentBlanklineIndent2 guifg=#720026 gui=nocombine]])
vim.cmd([[highlight IndentBlanklineIndent3 guifg=#CE4257 gui=nocombine]])
vim.cmd([[highlight IndentBlanklineIndent4 guifg=#FF7F51 gui=nocombine]])
vim.cmd([[highlight IndentBlanklineIndent5 guifg=#FF9B54 gui=nocombine]])

indent_blankline.setup({
	space_char_blankline = " ",
	show_current_context = true,
	char_highlight_list = {
		"IndentBlanklineIndent1",
		"IndentBlanklineIndent2",
		"IndentBlanklineIndent3",
		"IndentBlanklineIndent4",
		"IndentBlanklineIndent5",
	},
})
