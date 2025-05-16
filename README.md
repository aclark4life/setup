# Setup macOS and Linux

> "It's almost too easy." —Alex

Based on (RIP):

- https://github.com/aclark4life/setup-macos
- https://github.com/aclark4life/setup-linux

## Oh My ZSH

```bash
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

## Homebrew

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## PyEnv

> [!NOTE]
> `pyenv` will select the latest stable version of Python 3

### macOS

```bash
/opt/homebrew/bin/brew install pyenv
/opt/homebrew/bin/pyenv install 3
/opt/homebrew/bin/pyenv global 3
```

### Linux
```bash
/home/linuxbrew/.linuxbrew/bin/brew install pyenv
/home/linuxbrew/.linuxbrew/bin/pyenv install 3
/home/linuxbrew/.linuxbrew/bin/pyenv global 3
```

## PipX

```bash
.pyenv/shims/pip install pipx
.pyenv/shims/pipx install dotfiles 
.pyenv/shims/pipx install checkoutmanager
.pyenv/shims/pipx install pre-commit
.pyenv/shims/pipx install pypistats
.pyenv/shims/pipx install uv
```

## Create key
```bash
ssh-keygen -t ed25519 -f ~/.ssh/id
```

## Dotfiles

Via [dotfiles](https://github.com/aclark4life/dotfiles).

### Clone

```bash
git clone https://github.com/aclark4life/dotfiles Dotfiles
.local/bin/dotfiles -sf
```

### Copy key

```bash
pbcopy < ~/.ssh/id.pub
```

### Add key

> [!NOTE]
> You will need your GitHub account information for this step.

[Add a new key to GitHub](https://github.com/settings/ssh/new)!

### Fix remote

```bash
cd ~/Dotfiles
git remote remove origin
git remote add origin git@github.com:aclark4life/dotfiles.git
git push --set-upstream origin main
```

## Firefox

### Extensions

- [Bitwarden](https://addons.mozilla.org/en-US/firefox/addon/bitwarden-password-manager/)
- [Colorzilla](https://addons.mozilla.org/en-US/firefox/addon/colorzilla/)
- [Measure-it](https://addons.mozilla.org/en-US/firefox/addon/measure-it/)

### Disable Firefox tab hover preview

> [!NOTE]
>
> [Tab previews are annoying](https://connect.mozilla.org/t5/discussions/tab-previews-are-annoying/m-p/64519#M22742)

[Open config](http://about:config)

Set to false:

```
browser.tabs.hoverPreview.enabled
```

## Chrome

### Extensions

- [Bitwarden](https://chromewebstore.google.com/detail/bitwarden-password-manage/nngceckbapebfimnlniiiahkandclblb)
- [Video Speed Controller](https://chromewebstore.google.com/detail/video-speed-controller/nffaoalbilbmmfgbnbgppjihopabppdk?hl=en)

## VS Code

- [VS Code](https://code.visualstudio.com/sha/download?build=stable&os=darwin-universal)
- [Copilot](https://code.visualstudio.com/docs/copilot/setup#_step-2-install-the-github-copilot-extension)

## Neovim

- [Copilot](https://github.com/github/copilot.vim)

## pCloud

- https://www.pcloud.com/how-to-install-pcloud-drive-apple-silicon.html?download=macm1

## nvm

> [!NOTE]
> 
> Installed by Homebrew, used to install `m`

```
nvm install 22
nvm use 22
```

> [!NOTE]
>
> MongoDB Version Management

## m

```
npm install -g m
m stable
mo start
ml single
```

## Brew services

> [!NOTE]
>
> Start postgresql

```
brew services start postgresql
```

## Terminal

> [!NOTE]
> 
> Increase the font size 4 times

- ⌘ ++++

> [!NOTE]
> 
> Save as default

- Terminal → Shell → Use Settings as Default

### Preferences…

#### Profiles → Advanced → Bell

- ☐ Audible bell 
- ☐ Visual bell 
- ☐ Badge app and window Dock 
- ☐ Bounce app icon when in background 

#### Profiles → Shell

- [Close the window] When the shell exits
- [Never] Ask before closing

#### Profiles → Window

> [!NOTE]
> 
> Window size x 1.5

- Window Size → Columns → 120
- Window Size → Rows → 36

## System Preferences

> [!NOTE]
> Click your way to the finish!
>
> Ideally this would be done with [defaults write](https://github.com/aclark4life/setup-macos/blob/40eee1aad8bd0e1aa6926af9751f95f905fd89d8/project.mk#L3-L11).

### Accessibility

- Zoom → ☑︎ Use scroll gesture with modifier keys to zoom: [^Control]

### Battery

- Battery → Turn display off after [Never]
- Battery → ☐ Slightly dim the display when on battery power
- Battery → ☐ Enable Power Nap while on battery power
- Power Adapter → Turn display off after [Never]
- Power Adapter → ☐ Enable Power Nap while plugged into a power adapter

### Bluetooth

- ☑︎ Show Bluetooth in menu bar

### Desktop & Screen Saver

- Desktop

### Displays

- ☐ Automatically adjust brightness

### Dock & Menu Bar

- Dock & Menu Bar → ☐ Show recent applications in Dock

### Keyboard

- Input Sources → ☑︎ Show input menu in menu bar
- Shortcuts → Mission Control → ☑︎ Move left a space [⌘←]
- Shortcuts → Mission Control → ☑︎ Move right a space [⌘→]

### Mission Control

- Keyboard and Mouse Shortcuts → Mission Control → Middle Mouse Button
- ☐ Displays have separate spaces

### Security & Privacy

- General → A login password has been set for this user → ☐ Require password

### Trackpad

- More Gestures → ☐ Swipe between pages

### Users & Groups

- alexclark → Login Items → + Jumpcut
- alexclark → Login Items → + pCloud Drive
- Login Options → Automatic Login → alexclark

[Back to top](#table-of-contents)
