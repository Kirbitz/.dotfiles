# .Dotfiles Repo

A repo to host all of my dotfile configs

### Using smlinksetup

Setup File Flags

- -n = Nvim
- -p = Picom
- -q = Qtile
- -z = ZSH

Setup will also prompt the user before removing/modifying existing directories/files

After all other files have been cleared the symlinks will be setup

Once finished the setup will be all good to go

#### **Example**

    ./smlinksetup.sh -npqz
