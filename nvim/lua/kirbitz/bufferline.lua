local status_ok, bufferline = pcall(require, "bufferline")
if not status_ok then
  vim.notify("Bufferline failed to load!", vim.log.levels.ERROR, { title = "Package Failure" })
  return
end

bufferline.setup({
  options = {
    number = "none",
    close_command = "Bdelete! %d",
    right_mouse_command = "Bdelete! %d",
    left_mouse_command = "buffer %d",
    middle_mouse_command = nil,
    indicator = {
      icon = "▊",
      style = "icon",
    },
    buffer_close_icon = "",
    modified_icon = "",
    left_trunc_marker = "",
    right_trunc_marker = "",
    max_name_length = 30,
    max_prefix_length = 30,
    tab_size = 21,
    diagnostics = false,
    diagnostics_update_in_insert = false,
    offsets = {
      {
        filetype = "NvimTree",
        text = "File Explorer",
        highlight = "Directory",
        text_align = "left",
        separator = true,
      },
    },
    show_buffer_icons = true,
    show_buffer_close_icons = true,
    show_close_icon = true,
    show_tab_indicators = true,
    persist_buffer_sort = true,
    separator_style = "thin",
    enforce_regular_tabs = true,
    always_show_bufferline = true,
  },
})
