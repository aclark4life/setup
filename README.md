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
/opt/homebrew/bin/pyenv install 3.14
/opt/homebrew/bin/pyenv global 3.14
```

**Linux Setup:**

```bash
/home/linuxbrew/.linuxbrew/bin/brew install pyenv
/home/linuxbrew/.linuxbrew/bin/pyenv install 3.14
/home/linuxbrew/.linuxbrew/bin/pyenv global 3.14
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

macOS:

```bash
pbcopy < ~/.ssh/id.pub
```

Linux:

```bash
wl-copy < ~/.ssh/id.pub
```

**3. GitHub Configuration:**

- [Add new key to GitHub](https://github.com/settings/ssh/new)

**4. Clone and Link:**

> [!NOTE]
> `~/Dotfiles/ssh` only tracks `config`, so `dotfiles -sf` replaces `~/.ssh`
> with a symlink to it. Back up your key first, then restore it after
> syncing.

```bash
mkdir -p ~/ssh-backup
cp ~/.ssh/id ~/.ssh/id.pub ~/ssh-backup/
git clone https://github.com/aclark4life/dotfiles Dotfiles
.local/bin/dotfiles -sf
cp ~/ssh-backup/id ~/ssh-backup/id.pub ~/.ssh/
chmod 600 ~/.ssh/id
rm -rf ~/ssh-backup
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

Open the extension pages (click "Add to Firefox" on each tab):

```bash
OPEN="$(command -v open || command -v xdg-open)"
for url in \
  "https://addons.mozilla.org/en-US/firefox/addon/bitwarden-password-manager/" \
  "https://addons.mozilla.org/en-US/firefox/addon/colorzilla/" \
  "https://addons.mozilla.org/en-US/firefox/addon/measure-it/" \
  "https://addons.mozilla.org/en-US/firefox/addon/videospeed/"; do
  "$OPEN" "$url"
done
```

- **Disable Tab Previews:** Sets `browser.tabs.hoverPreview.enabled` to `false` without visiting `about:config` manually. Close Firefox first.

```bash
profile_dir="$(find ~/Library/Application\ Support/Firefox/Profiles ~/.mozilla/firefox -maxdepth 1 -name '*.default*' 2>/dev/null | head -1)"
echo 'user_pref("browser.tabs.hoverPreview.enabled", false);' >> "$profile_dir/user.js"
```

### Chrome

- **Extensions:** [Bitwarden](https://chromewebstore.google.com/detail/bitwarden-password-manage/nngceckbapebfimnlniiiahkandclblb), [Video Speed Controller](https://chromewebstore.google.com/detail/video-speed-controller/nffaoalbilbmmfgbnbgppjihopabppdk?hl=en)

Open the extension pages (click "Add to Chrome" on each tab):

```bash
OPEN="$(command -v open || command -v xdg-open)"
for url in \
  "https://chromewebstore.google.com/detail/bitwarden-password-manage/nngceckbapebfimnlniiiahkandclblb" \
  "https://chromewebstore.google.com/detail/video-speed-controller/nffaoalbilbmmfgbnbgppjihopabppdk?hl=en"; do
  "$OPEN" "$url"
done
```

---

## Development Tools

**pCloud:** [Download pCloud Drive](https://www.pcloud.com/download-free-online-cloud-file-storage)

**Neovim Copilot:**

```bash
git clone https://github.com/github/copilot.vim ~/.config/nvim/pack/github/start/copilot.vim
```

**Node (nvm):**

```bash
nvm install 24
nvm use 24
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
> Access and will prompt as needed. Once dotfiles are linked, run it via the
> `macprefs` alias.

```bash
macprefs
```
