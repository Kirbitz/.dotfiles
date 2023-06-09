# Created by Zap installer
[ -f "$HOME/.local/share/zap/zap.zsh" ] && source "$HOME/.local/share/zap/zap.zsh"
plug "zsh-users/zsh-autosuggestions"
plug "zap-zsh/supercharge"
plug "zsh-users/zsh-syntax-highlighting"
plug "chivalryq/git-alias"
plug "hlissner/zsh-autopair"

export PATH=$PATH:/home/kirbitz/wyvern/bin
export PATH=$PATH:/usr/local/zig
export PATH=$PATH:/home/kirbitz/.nimble/bin
export PATH=$PATH:/usr/local/go/bin
export PATH=$PATH:/usr/local/julia-1.6.7/bin
source /home/kirbitz/.ghcup/env
source /home/kirbitz/.sdkman/bin/sdkmain-init.sh


alias la="ls -a"
alias rm="rm -i"
alias mv="mv -i"
alias cp="cp -i"

autoload -Uz vcs_info
autoload -U colors && colors

zstyle ':vcs_info:*' enable git 

precmd_vcs_info() { vcs_info }
precmd_functions+=( precmd_vcs_info )
setopt prompt_subst


zstyle ':vcs_info:git*+set-message:*' hooks git-untracked

+vi-git-untracked(){
    if [[ $(git rev-parse --is-inside-work-tree 2> /dev/null) == 'true' ]] && \
        git status --porcelain | grep '??' &> /dev/null ; then
        hook_com[staged]+='!' # signify new files with a bang
    fi
}

zstyle ':vcs_info:*' check-for-changes true
zstyle ':vcs_info:git:*' formats " %B%{$fg[blue]%}(%{$fg[red]%}%m%u%c%{$fg[yellow]%}%{$fg[magenta]%} %b%{$fg[blue]%})%{$reset_color%}"

PROMPT="%B%F{magenta}[%F{white}$USERNAME%F{magenta}] % %(?:%{$fg_bold[green]%}ﰲ :%{$fg_bold[red]%}ﰲ )%{$fg[cyan]%}%c%{$reset_color%}"
PROMPT+="\$vcs_info_msg_0_ "

neofetch --jp2a ~/Documents/logo/Kirby.jpg --colors 5 7 1 5 7 7

[ -f "/home/kirbitz/.ghcup/env" ] && source "/home/kirbitz/.ghcup/env" # ghcup-env

#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="$HOME/.sdkman"
[[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ]] && source "$HOME/.sdkman/bin/sdkman-init.sh"
