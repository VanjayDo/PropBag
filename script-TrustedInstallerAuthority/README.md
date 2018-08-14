# TrustedInstaller权限注册与删除

### 说明
为方便在windows中获取文件的TrustedInstaller权限, 创建了这两个小脚本.

### 使用方法
运行`RegistTrustedInstallerAuthority.reg`即可在注册表中注册TrustedInstaller权限的右击快捷键, 成功后在任何文件上右击即可看到`Get TrustedInstaller Authority`字样, 点击即可获取该文件的TrustedInstaller权限.

运行`DeleteTrustedInstallerAuthority.reg`即可从注册表中删除该右击快捷键.