Third Party Apps (DEPRECATED)
=============================

**Note**: This repo will not accept NEW packages as we are replacing the majority of them in Solus with Snaps. After we have Snaps integrated in the Software Center we will begin forceful deprecation of this repository.

**Note**: The Solus ThirdParty repo will not accept NEW packages as they are replacing the
majority of them in Solus with Snaps. After the Ubuntu Rally (NYC) at the
end of September 2017, they will have Snaps integrated in the Software Center,
and will begin forceful deprecation of this repository.

This repo contains the build files required to create packages that cannot be redistributed, whether for licensing restrictions or otherwise.

Even with the support of Snaps not all of this apllication will be avalible on Solus.

Even with the support of Snaps not all of this apllication will be avalible on Solus.

For more information about 3rd party applications in Solus, visit our Help Center page at https://getsol.us/articles/software/third-party/en/.



DO NOT PUSH BINARY PACKAGES! The git history has been reset because it ballooned
to nearly 300MB in size. :)




# Third Party

The following applications are provided via our 3rd Party Repository 
to facilitate the installation and usage of them. These applications 
cannot be included in the primary repository due to licensing issues.

Alongside the following commands, you may also find some of these 
applications via the Third Party section on our Software Center.

If these instructions fail to work please [file an issue](ttps://github.com/getsolus/3rd-Party). To upgrade once installed simply run the commands again. If there is a new version it will be installed.

This list is based of
* https://github.com/getsolus/3rd-party
* https://getsol.us/articles/software/third-party/en/

## Browsers

### Google Chrome
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/network/web/browser/google-chrome-stable/pspec.xml
sudo eopkg it google-chrome-*.eopkg;sudo rm google-chrome-*.eopkg
```

### Google Chrome (Beta)
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/network/web/browser/google-chrome-beta/pspec.xml
sudo eopkg it google-chrome-*.eopkg;sudo rm google-chrome-*.eopkg
```

### Google Chrome (Dev/Unstable)
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/network/web/browser/google-chrome-unstable/pspec.xml
sudo eopkg it google-chrome-*.eopkg;sudo rm google-chrome-*.eopkg
```

## Communication

### Franz

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/network/im/franz/pspec.xml
sudo eopkg it franz*.eopkg;sudo rm franz*.eopkg
```

### Google Talk Browser Plugin

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/network/im/google-talkplugin/pspec.xml
sudo eopkg it google-talkplugin*.eopkg;sudo rm google-talkplugin*.eopkg
```

### Skype for Linux
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/network/im/skype/pspec.xml
sudo eopkg it skype*.eopkg;sudo rm *.eopkg
```

### Slack
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/network/im/slack-desktop/pspec.xml
sudo eopkg it slack-desktop*.eopkg;sudo rm slack-desktop*.eopkg
```

### Viber

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/network/im/viber/pspec.xml
sudo eopkg it viber*.eopkg;sudo rm *.eopkg
```

## Multimedia

### Adobe Flash Player (NPAPI)

The NPAPI version of Adobe Flash Player is typically used with Firefox.

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/multimedia/video/flash-player-npapi/pspec.xml
sudo eopkg it flash-player-npapi*.eopkg;sudo rm flash-player-npapi*.eopkg
```

### Adobe Flash Player (PPAPI)

The PPAPI version of Adobe Flash Player is typically used with Vivaldi. Chrome provides its own Flash.

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/multimedia/video/flash-player-ppapi/pspec.xml
sudo eopkg it flash-player-ppapi*.eopkg;sudo rm flash-player-ppapi*.eopkg
```

### Bitwig Studio

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/multimedia/music/bitwig-studio/pspec.xml
sudo eopkg it bitwig-studio*.eopkg;sudo rm bitwig-studio*.eopkg
```

### OcenAudio
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/multimedia/music/ocenaudio/pspec.xml
sudo eopkg it ocenaudio*.eopkg;sudo rm ocenaudio*.eopkg
```

### Pixeluvo

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/multimedia/graphics/pixeluvo/pspec.xml
sudo eopkg it pixeluvo*.eopkg;sudo rm pixeluvo*.eopkg
```

### Plex Media Server
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/multimedia/video/plexmediaserver/pspec.xml
sudo eopkg it plexmediaserver-*.eopkg;sudo rm plexmediaserver-*.eopkg
sudo systemd-tmpfiles --create
sudo systemctl start plexmediaserver.service
```

**Note:** Optionally have it start on boot:

```bash
sudo systemctl <span class="hljs-built_in">enable</span> plexmediaserver.service
```

### Sunvox

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/multimedia/music/sunvox/pspec.xml
sudo eopkg it sunvox*.eopkg;sudo rm sunvox*.eopkg
```

### Spotify
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/multimedia/music/spotify/pspec.xml
sudo eopkg it spotify*.eopkg;sudo rm spotify*.eopkg
```

## Network

### AnyDesk

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/network/util/anydesk/pspec.xml
sudo eopkg it anydesk*.eopkg;sudo rm anydesk*.eopkg
```

### Insync

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/network/download/insync/pspec.xml
sudo eopkg it insync*.eopkg;sudo rm insync*.eopkg
```

### Spideroak

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/network/download/spideroak/pspec.xml
sudo eopkg it spideroak*.eopkg;sudo rm spideroak*.eopkg
```

### Synology Cloud Station Drive

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/network/download/synology-cloud-station-drive/pspec.xml
sudo eopkg it synology-cloud-station-drive*.eopkg;sudo rm synology-cloud-station-drive*.eopkg
```

### TeamViewer

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/network/util/teamviewer/pspec.xml
sudo eopkg it teamviewer*.eopkg;sudo rm teamviewer*.eopkg
sudo systemctl start teamviewerd.service
```

## Office

### Mendeley Desktop

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/office/mendeleydesktop/pspec.xml
sudo eopkg it mendeleydesktop*.eopkg;sudo rm mendeleydesktop*.eopkg
```

### Microsoft Core Fonts

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/desktop/font/mscorefonts/pspec.xml
sudo eopkg it mscorefonts*.eopkg;sudo rm mscorefonts*.eopkg
```

### Moneydance
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/office/moneydance/pspec.xml
sudo eopkg it moneydance*.eopkg;sudo rm moneydance*.eopkg
```

### PomoDoneApp

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/office/pomodoneapp/pspec.xml
sudo eopkg it pomodoneapp*.eopkg;sudo rm pomodoneapp*.eopkg
```

### Scrivener

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/office/scrivener/pspec.xml
sudo eopkg it scrivener*.eopkg;sudo rm scrivener*.eopkg
```

### WPS Office
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/office/wps-office/pspec.xml
sudo eopkg it wps-office*.eopkg;sudo rm wps-office*.eopkg
```

### Softmaker Office
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/office/softmaker-office/pspec.xml
sudo eopkg it softmaker-office*.eopkg;sudo rm softmaker-office*.eopkg
```

### Programming

### Android Studio
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/programming/android-studio/pspec.xml
sudo eopkg it android-studio*.eopkg;sudo rm android-studio*.eopkg
```

### Android Tools

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/programming/tools/android-tools/pspec.xml
sudo eopkg it android-tools*.eopkg;sudo rm android-tools*.eopkg
```

### CLion
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/programming/clion/pspec.xml
sudo eopkg it clion*.eopkg;sudo rm clion*.eopkg
```

### Datagrip
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/programming/datagrip/pspec.xml
sudo eopkg it datagrip*.eopkg;sudo rm datagrip*.eopkg
```

### GitKraken
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/programming/gitkraken/pspec.xml
sudo eopkg it gitkraken*.eopkg;sudo rm gitkraken*.eopkg
```

### IDEA
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/programming/idea/pspec.xml
sudo eopkg it idea*.eopkg;sudo rm idea*.eopkg
```

### GoLand
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/programming/goland/pspec.xml
sudo eopkg it goland*.eopkg;sudo rm goland*.eopkg
```

### PHPStorm
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/programming/phpstorm/pspec.xml
sudo eopkg it phpstorm*.eopkg;sudo rm phpstorm*.eopkg
```

### PyCharm Community Edition
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/programming/pycharm-ce/pspec.xml
sudo eopkg it pycharm-ce*.eopkg;sudo rm pycharm-ce*.eopkg
```

### Pycharm
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/programming/pycharm/pspec.xml
sudo eopkg it pycharm*.eopkg;sudo rm pycharm*.eopkg
```

### Rider
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/programming/rider/pspec.xml
sudo eopkg it rider*.eopkg;sudo rm rider*.eopkg
```

### RubyMine
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/programming/rubymine/pspec.xml
sudo eopkg it rubymine*.eopkg;sudo rm rubymine*.eopkg
```

### Sublime Text 3
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/programming/sublime-text-3/pspec.xml
sudo eopkg it sublime*.eopkg;sudo rm sublime*.eopkg
```

### WebStorm
**SNAPED** 
```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/programming/webstorm/pspec.xml
sudo eopkg it webstorm*.eopkg;sudo rm webstorm*.eopkg
```

## Security

### Enpass

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/security/enpass/pspec.xml
sudo eopkg it enpass*.eopkg;sudo rm enpass*.eopkg
```

## Other

### Google Earth

```bash
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/ctieben/3rd-party/master/network/web/google-earth/pspec.xml
sudo eopkg it google-earth*.eopkg;sudo rm google-earth*.eopkg
```

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> acb70e5 (Mark snaped packages and list other applications on snap)
## To be done
* GanttProject
* FreeOffice
* SoftMaker Office Standard / Professional


<<<<<<< HEAD
# Apps by [Snap](https://snapcraft.io/store)
=======
# Apps by [https://snapcraft.io/store](Snap)
>>>>>>> acb70e5 (Mark snaped packages and list other applications on snap)
* Skype
* Spotify
* Slack
* Telegram
* Signal Desktop
* Discord
* Zenkit
* Bitwarden
* OnlyOffice
* Nextcloud
* Atom
* Visual Studio Code
* Jetbrains Software
* NetBeans
* GitKraken



