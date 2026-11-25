# Setup macOS and Linux

See also: [aclark4life/dotfiles](https://github.com/aclark4life/dotfiles).

## sudo

```bash
echo "alex.clark ALL=(ALL) NOPASSWD: ALL" | sudo EDITOR='tee -a' visudo
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

## Browsers & Extensions

### Firefox

- **Extensions:** [Bitwarden](https://addons.mozilla.org/en-US/firefox/addon/bitwarden-password-manager/), [Colorzilla](https://addons.mozilla.org/en-US/firefox/addon/colorzilla/), [Measure-it](https://addons.mozilla.org/en-US/firefox/addon/measure-it/), [Video Speed Controller](https://addons.mozilla.org/en-US/firefox/addon/videospeed/)

Open the extension pages in Firefox (click "Add to Firefox" on each tab):

```bash
open_in_firefox() { command -v firefox >/dev/null && firefox "$1" || open -a Firefox "$1"; }
open_in_firefox "https://addons.mozilla.org/en-US/firefox/addon/bitwarden-password-manager/"
open_in_firefox "https://addons.mozilla.org/en-US/firefox/addon/colorzilla/"
open_in_firefox "https://addons.mozilla.org/en-US/firefox/addon/measure-it/"
open_in_firefox "https://addons.mozilla.org/en-US/firefox/addon/videospeed/"
```

### Chrome

- **Extensions:** [Bitwarden](https://chromewebstore.google.com/detail/bitwarden-password-manage/nngceckbapebfimnlniiiahkandclblb), [Video Speed Controller](https://chromewebstore.google.com/detail/video-speed-controller/nffaoalbilbmmfgbnbgppjihopabppdk?hl=en)

Open the extension pages in Chrome (click "Add to Chrome" on each tab):

```bash
open_in_chrome() { command -v google-chrome >/dev/null && google-chrome "$1" || open -a "Google Chrome" "$1"; }
open_in_chrome "https://chromewebstore.google.com/detail/bitwarden-password-manage/nngceckbapebfimnlniiiahkandclblb"
open_in_chrome "https://chromewebstore.google.com/detail/video-speed-controller/nffaoalbilbmmfgbnbgppjihopabppdk?hl=en"
```

### Safari

- **Extensions:** [Bitwarden](https://apps.apple.com/us/app/bitwarden-password-manager/id1352778147)

Open the extension page in Safari (click "View in Mac App Store" / install via the App Store, then enable it in Safari > Settings > Extensions):

```bash
open_in_safari() { open -a Safari "$1"; }
open_in_safari "https://apps.apple.com/us/app/bitwarden-password-manager/id1352778147"
```

> [!NOTE]
> For Safari/macOS to use Bitwarden instead of iCloud Keychain for
> AutoFill, go to **System Settings > General > AutoFill & Passwords**,
> enable Bitwarden as an allowed AutoFill extension, and set it as the
> default password manager.

> [!WARNING]
> On newer macOS versions, Bitwarden ships two separate Safari
> integrations: a Password AutoFill Provider and a full Safari Web
> Extension. If only the "Passwords" entry shows as available (the full
> extension is missing or greyed out), it's a known Bitwarden/macOS
> compatibility gap, not a local setup issue — check the Mac App Store /
> Bitwarden desktop app for updates and retry.

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

## Remote Desktop (macOS → Zorin/GNOME)

Use **GNOME Desktop Sharing** (RDP into the logged-in session) on the Linux
host and Microsoft's [Windows App](https://apps.apple.com/us/app/windows-app/id1295203466)
on macOS. Avoid xrdp (separate X11 session, poor experience) and GNOME
**Remote Login** (its server handover doesn't work with Windows App on
macOS: the second login always fails).

**1. Enable auto-login and disable Remote Login** (so Desktop Sharing
gets port 3389):

```bash
sudo sed -i "s/^#\? *AutomaticLoginEnable.*/AutomaticLoginEnable=true/; s/^#\? *AutomaticLogin *=.*/AutomaticLogin=$USER/" /etc/gdm3/custom.conf
sudo grdctl --system rdp disable
sudo reboot
```

**2. Blank the keyring password and enable Desktop Sharing:**

Desktop Sharing reads its credentials from the GNOME login keyring, which
auto-login leaves locked. [`gnome-desktop-sharing.py`](gnome-desktop-sharing.py)
sets the keyring password to empty (so it unlocks with auto-login), then
sets the RDP credentials, enables remote control and starts the service. It
prompts for passwords, so nothing is logged.

```bash
scp gnome-desktop-sharing.py <host>:/tmp/
ssh -t <host> /tmp/gnome-desktop-sharing.py
```

> [!WARNING]
> A blank keyring password stores saved secrets (browser and Wi-Fi
> passwords, app tokens) unencrypted on disk.

> [!NOTE]
> The keyring password can differ from the login password (e.g. after
> changing the login password with `passwd`). If the script says the
> password is invalid, try an older login password.

**3. Connect from macOS:**

- Windows App → **+** → **Add PC**, using the host's IP address or
  fully-qualified name (e.g. `<host>.<router-domain>`). Windows App
  ignores DNS search domains, so a bare hostname fails with error 0x104
  even when `ssh <host>` works.
- Allow Windows App in **System Settings > Privacy & Security > Local
  Network**.
- Use the RDP username and password set in step 2.

> [!CAUTION]
> Don't pass credentials to `sudo grdctl --system rdp set-credentials` on
> the command line: `sudo` and `pkexec` log the full command, password
> included, to the system journal. With no TPM, `grdctl --system` also
> stores credentials in a file that the running daemon only reads at
> startup, so restart `gnome-remote-desktop` after changing them.

## Other Software

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
