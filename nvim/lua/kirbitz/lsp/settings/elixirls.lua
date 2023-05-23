local path_to_elixir = vim.fn.expand("~/elixir-ls/release/language_server.sh")

return {
	cmd = { path_to_elixir },
	settings = {
		elixirLS = {
			dialyzerEnabled = false,
			fetchDeps = false,
		},
	},
}
