local status_mason_dap_ok, mason_dap = pcall(require, "mason-nvim-dap")
if not status_mason_dap_ok then
	vim.notify("Mason DAP failed to load!", vim.log.levels.ERROR, { title = "Package Failure" })
	return
end

local status_dap_ok, dap = pcall(require, "dap")
if not status_dap_ok then
	vim.notify("DAP failed to load!", vim.log.levels.ERROR, { title = "Package Failure" })
	return
end

local status_dapui_ok, dapui = pcall(require, "dapui")
if not status_dapui_ok then
	vim.notify("DAP failed to load!", vim.log.levels.ERROR, { title = "Package Failure" })
	return
end

mason_dap.setup({
	ensure_installed = { "python" },

	automatic_installation = true,

	handlers = {
		function(config)
			mason_dap.default_setup(config)
		end,
		python = function(config)
			config.adapters = {
				type = "executable",
				command = "/usr/bin/python3",
				args = {
					"-m",
					"debugpy.adapter",
				},
			}
			dap.configurations.python = {
				{
					type = "python",
					request = "launch",
					name = "Launch file",
					program = "${file}",
				},
			}
			mason_dap.default_setup(config)
		end,
	},
})

dapui.setup()

dap.listeners.after.event_initialized["dapui_config"] = function()
	dapui.open()
end

dap.listeners.before.event_terminated["dapui_config"] = function()
	dapui.close()
end

dap.listeners.before.event_exited["dapui_config"] = function()
	dapui.close()
end
