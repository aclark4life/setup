# Setup macOS and Linux

## sudo

Run `sudo visudo` and add an entry for `alex.clark`:

```text
alex.clark ALL=(ALL) NOPASSWD: ALL
```

## Homebrew & Oh My ZSH

| Step | macOS | Linux |
| :--- | :--- | :--- |
| **Homebrew** | `bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` | Same as macOS |
| **Oh My ZSH** | `sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"` | Install `zsh` first, `chsh` to zsh, then run install script |

## PyEnv

| Platform | Command |
| :--- | :--- |
| **macOS** | `/opt/homebrew/bin/brew install pyenv && /opt/homebrew/bin/pyenv install 3.13 && /opt/homebrew/bin/pyenv global 3.13` |
| **Linux** | `/home/linuxbrew/.linuxbrew/bin/brew install pyenv && /home/linuxbrew/.linuxbrew/bin/pyenv install 3.13 && /home/linuxbrew/.linuxbrew/bin/pyenv global 3.13` |

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
> Reference: [aclark4life/dotfiles](https://github.com/aclark4life/dotfiles)

1. **Create SSH Key:**
   ```bash
   ssh-keygen -t ed25519 -f ~/.ssh/id
   ```

2. **Copy Public Key:**
   | Platform | Command |
   | :--- | :--- |
   | **macOS** | `pbcopy < ~/.ssh/id.pub` |
   | **Linux** | `wl-copy < ~/.ssh/id.pub` |

3. **GitHub Setup:**
   * [Add the new key to GitHub](https://github.com/settings/ssh/new)

4. **Clone & Link:**
   ```bash
   git clone https://github.com/aclark4life/dotfiles Dotfiles
   .local/bin/dotfiles -sf
   ```

5. **Fix Remote:**
   ```bash
   cd ~/Dotfiles
   git remote remove origin
   git remote add origin git@github.com:aclark4life/dotfiles.git
   git push --set-upstream origin main
   ```

---

## Browsers

### Firefox
* **Extensions:** [Bitwarden](https://addons.mozilla.org/en-US/firefox/addon/bitwarden-password-manager/), [Colorzilla](https://addons.mozilla.org/en-US/firefox/addon/colorzilla/), [Measure-it](https://addons.mozilla.org/en-US/firefox/addon/measure-it/)
* **Disable Tab Previews:** Open `about:config` and set `browser.tabs.hoverPreview.enabled` to **false**.

### Chrome
* **Extensions:** [Bitwarden](https://chromewebstore.google.com/detail/bitwarden-password-manage/nngceckbapebfimnlniiiahkandclblb), [Video Speed Controller](https://chromewebstore.google.com/detail/video-speed-controller/nffaoalbilbmmfgbnbgppjihopabppdk?hl=en)

---

## Development Tools

### VS Code & Neovim
* [VS Code Stable](https://code.visualstudio.com/sha/download?build=stable&os=darwin-universal)
* [Copilot for VS Code](https://code.visualstudio.com/docs/copilot/setup#_step-2-install-the-github-copilot-extension)
* **Neovim Copilot:**
    ```bash
    git clone https://github.com/github/copilot.vim ~/.config/nvim/pack/github/start/copilot.vim
    ```

### Node & Tools
* **nvm:** `nvm install 22 && nvm use 22`
* **m:** `npm install -g m && m stable`
* **pCloud:** [Apple Silicon Driver](https://www.pcloud.com/how-to-install-pcloud-drive-apple-silicon.html?download=macm1)
* **xeyes:** Run `xeyes -geometry 300x400` from an `xterm` (via XQuartz).

---

## macOS Specific Settings

### Terminal
* **Font Size:** `⌘` + `++++`
* **Persistence:** Terminal → Shell → Use Settings as Default

| Category | Setting | Requirement |
| :--- | :--- | :--- |
| **Profiles → Advanced** | Bell | Uncheck: Audible, Visual, Badge, and Bounce |
| **Profiles → Shell** | Window Closing | [Close the window] When shell exits; [Never] Ask before closing |
| **Profiles → Window** | Window Size | Columns: 120, Rows: 36 |

### System Preferences

| Section | Preference |
| :--- | :--- |
| **Accessibility** | Zoom → Use scroll gesture with modifier keys [^Control] |
| **Battery** | Disable "Slightly dim" and "Power Nap"; Display off: [Never] |
| **Bluetooth** | Show in menu bar |
| **Displays** | Disable "Automatically adjust brightness" |
| **Dock** | Disable "Show recent applications" |
| **Keyboard** | Shortcuts → Mission Control → Move Space Left/Right [⌘← / ⌘→] |
| **Lock Screen** | Turn display off [Never] |
| **Mission Control** | Middle Mouse Button for MC; Disable "Displays have separate spaces" |
| **Security** | General → Require password [Uncheck] |
| **Trackpad** | Disable "Swipe between pages" |
| **Users & Groups** | Login Items: + Jumpcut, + pCloud; Automatic Login: alexclark |
