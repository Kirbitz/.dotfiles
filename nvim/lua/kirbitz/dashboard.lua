local status_ok, dashboard = pcall(require, "dashboard")
if not status_ok then
	vim.notify("Failed to Load Dashboard Nvim", vim.log.levels.ERROR, { title = "Package Failure" })
	return
end

dashboard.setup({
	theme = "hyper",
	change_to_vcs_root = true,
	config = {
		week_header = {
			enable = true,
			concat = "Happy Coding! ",
		},
		shortcut = {
			{
				desc = " Explore",
				group = "@property",
				action = "NvimTreeToggle",
				key = "e",
			},
			{
				icon = " ",
				icon_hl = "@variable",
				desc = "Files",
				group = "Label",
				action = "Telescope find_files",
				key = "f",
			},
			{
				desc = " Search Repos",
				group = "DiagnosticError",
				action = "Telescope repo list",
				key = "r",
			},
			{
				desc = "ﲴ Check LSPs",
				group = "DiagnosticHint",
				action = "Mason",
				key = "m",
			},
			{
				desc = " Open Terminal",
				group = "DiagnosticWarn",
				action = "ToggleTerm",
				key = "t",
			},
		},
		packages = {
			enable = true,
		},
	},
})
