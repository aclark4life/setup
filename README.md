# Setup macOS and Linux

## sudo

```bash
echo "alexclark ALL=(ALL) NOPASSWD: ALL" | sudo EDITOR='tee -a' visudo
```

## Package Managers & Shell

Standard install for both **Homebrew** and **Oh My ZSH** on macOS and Linux.

> [!NOTE]
> On Linux, install `zsh` + `chsh` first.

**Homebrew Command:**

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Oh My ZSH Command:**

```bash
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

## PyEnv

**macOS Setup:**

```bash
/opt/homebrew/bin/brew install pyenv
/opt/homebrew/bin/pyenv install 3.13
/opt/homebrew/bin/pyenv global 3.13
```

**Linux Setup:**

```bash
/home/linuxbrew/.linuxbrew/bin/brew install pyenv
/home/linuxbrew/.linuxbrew/bin/pyenv install 3.13
/home/linuxbrew/.linuxbrew/bin/pyenv global 3.13
```

## PipX

```bash
.pyenv/shims/pip install -U pip
.pyenv/shims/pip install pipx
.pyenv/shims/pipx install checkoutmanager
.pyenv/shims/pipx install dotfiles
```

---

## Dotfiles & SSH

> [!NOTE]
> See [https://github.com/aclark4life/dotfiles](https://github.com/aclark4life/dotfiles)

**1. Create Key:**

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id
```

**2. Copy Key to Clipboard:**
| Platform | Command |
| :--- | :--- |
| **macOS** | `pbcopy < ~/.ssh/id.pub` |
| **Linux** | `wl-copy < ~/.ssh/id.pub` |

**3. GitHub Configuration:**

- [Add new key to GitHub](https://github.com/settings/ssh/new)

**4. Clone and Link:**

```bash
git clone https://github.com/aclark4life/dotfiles Dotfiles
.local/bin/dotfiles -sf
```

**5. Fix Remote:**

```bash
cd ~/Dotfiles
git remote remove origin
git remote add origin git@github.com:aclark4life/dotfiles.git
git push --set-upstream origin main
```

---

## Browsers & Extensions

### Firefox

- **Extensions:** [Bitwarden](https://addons.mozilla.org/en-US/firefox/addon/bitwarden-password-manager/), [Colorzilla](https://addons.mozilla.org/en-US/firefox/addon/colorzilla/), [Measure-it](https://addons.mozilla.org/en-US/firefox/addon/measure-it/), [Video Speed Controller](https://addons.mozilla.org/en-US/firefox/addon/videospeed/)

- **Disable Tab Previews:** Open `about:config` and set `browser.tabs.hoverPreview.enabled` to `false`.

### Chrome

- **Extensions:** [Bitwarden](https://chromewebstore.google.com/detail/bitwarden-password-manage/nngceckbapebfimnlniiiahkandclblb), [Video Speed Controller](https://chromewebstore.google.com/detail/video-speed-controller/nffaoalbilbmmfgbnbgppjihopabppdk?hl=en)

---

## Development Tools

| Tool        | Action / Link                                                                                                      |
| :---------- | :----------------------------------------------------------------------------------------------------------------- |
| **VS Code** | [Download Darwin Universal](https://code.visualstudio.com/sha/download?build=stable&os=darwin-universal)           |
| **Copilot** | [Install Extension](https://code.visualstudio.com/docs/copilot/setup#_step-2-install-the-github-copilot-extension) |
| **pCloud**  | [Apple Silicon Driver](https://www.pcloud.com/how-to-install-pcloud-drive-apple-silicon.html?download=macm1)       |

**Neovim Copilot:**

```bash
git clone https://github.com/github/copilot.vim ~/.config/nvim/pack/github/start/copilot.vim
```

**Node (nvm & m):**

```bash
nvm install 22
nvm use 22
npm install -g m
m stable
```

**xeyes:**

```bash
xeyes -geometry 300x400
```

---

## macOS System Preferences

> [!NOTE]
> Most settings below are applied automatically by
> [`macos-system-preferences.sh`](https://github.com/aclark4life/dotfiles/blob/main/macos-system-preferences.sh)
> in [dotfiles](https://github.com/aclark4life/dotfiles). It's safe to re-run
> (idempotent); a few settings require `sudo` or Accessibility/Full Disk
> Access and will prompt as needed.

```bash
~/Dotfiles/macos-system-preferences.sh
```

### Terminal (manual)

- **Font:** `⌘` + `++++`
- **Default:** Terminal → Shell → Use Settings as Default

| Category                | Setting | Requirement                                                 |
| :---------------------- | :------ | :---------------------------------------------------------- |
| **Profiles → Advanced** | Bell    | Uncheck all (Audible, Visual, Badge, Bounce)                |
| **Profiles → Shell**    | Closing | [Close window] when shell exits; [Never] ask before closing |
| **Profiles → Window**   | Size    | Columns: 120, Rows: 36                                      |

### System Settings (scripted)

| Section            | Setting                                                                    |
| :----------------- | :-------------------------------------------------------------------------- |
| **Accessibility**  | Zoom → ☑︎ Use scroll gesture with [^Control]                                 |
| **Battery**        | Power Adapter → Turn display off [Never]; Disable Power Nap                 |
| **Bluetooth**      | ☑︎ Show in menu bar                                                          |
| **Displays**       | ☐ Automatically adjust brightness                                           |
| **Dock**           | ☐ Show recent applications                                                  |
| **Keyboard**       | Shortcuts → Mission Control → Move left/right a space [⌘← / ⌘→]            |
| **Lock Screen**    | Turn display off [Never]                                                    |
| **Mission Control**| Ensure at least 4 desktops (spaces) exist                                    |
| **Users & Groups** | Login Items: + Jumpcut, + pCloud Drive                                       |

### System Settings (manual)

| Section            | Setting                                                       |
| :----------------- | :------------------------------------------------------------ |
| **Users & Groups** | Auto Login: alexclark (not scripted, for security)             |
