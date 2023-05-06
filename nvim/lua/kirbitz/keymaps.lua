local opts = { noremap = true, silent = true }

local keymap = vim.api.nvim_set_keymap

keymap("", "<Space>", "<Nop>", opts)
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- Better window navigation
keymap("n", "<C-h>", "<C-w>h", opts)
keymap("n", "<C-j>", "<C-w>j", opts)
keymap("n", "<C-k>", "<C-w>k", opts)
keymap("n", "<C-l>", "<C-w>l", opts)

-- Quick command for Lexplore
keymap("n", "<leader>e", ":NvimTreeToggle<cr>", opts)

-- Resize with arrows
keymap("n", "<C-Up>", ":resize -2<CR>", opts)
keymap("n", "<C-Down>", ":resize +2<CR>", opts)
keymap("n", "<C-Right>", ":vertical resize +2<CR>", opts)
keymap("n", "<C-Left>", ":vertical resize -2<CR>", opts)

-- Navigate Buffers
keymap("n", "<S-l>", ":bnext<cr>", opts)
keymap("n", "<S-h>", ":bprevious<cr>", opts)

-- Visual
-- Stay in indent mode
keymap("v", "<", "<gv", opts)
keymap("v", ">", ">gv", opts)

-- Move Text Up and Down
keymap("v", "<A-j>", ":m '>+1<CR>gv=gv", opts)
keymap("v", "<A-k>", ":m '<-2<CR>gv=gv", opts)
keymap("v", "p", '"_dP', opts)

-- Telescope Keymaps
keymap(
	"n",
	"<leader>fs",
	"<cmd>lua require'telescope.builtin'.find_files(require('telescope.themes').get_dropdown({ previewer = false }))<CR>",
	opts
)
keymap("n", "<leader>ff", "<cmd>lua require'telescope.builtin'.find_files(require('telescope.themes'))<CR>", opts)
keymap("n", "<leader>fm", "<cmd>Telescope media_files<CR>", opts)
keymap("n", "<leader>fr", "<cmd>Telescope repo list<CR>", opts)
keymap("n", "<C-t>", "<cmd>Telescope live_grep<CR>", opts)

-- Toggle Term Keymap
keymap("t", "<C-j><C-k>", "<C-\\><C-n>", opts)

-- Bufferline Keymaps
keymap("n", "<leader>d", ":Bdelete<CR>", opts)
keymap("n", "<leader>fd", ":Bdelete!<CR>", opts)

-- Formatting keymap
keymap("n", "<leader>p", ":Format<CR>", opts)

-- Split window Keymap
keymap("n", "<leader>v", ":vsplit<CR>", opts)

-- Trouble Keymaps
keymap("n", "<leader>tt", ":TroubleToggle<CR>", opts)
keymap("n", "<leader>qf", ":TroubleToggle<CR>", opts)

-- Gitsigns keymaps
keymap("n", "<leader>gd", ":Gitsigns diffthis<CR>", opts)

-- Dap Keymaps
keymap("n", "<leader>b", ":DapToggleBreakpoint<CR>", opts)
keymap("n", "<F5>", ":DapContinue<CR>", opts)
keymap("n", "<F10>", ":DapStepOver<CR>", opts)
keymap("n", "<F11>", ":DapStepInto<CR>", opts)
keymap("n", "<F12>", ":DapStepOut<CR>", opts)
