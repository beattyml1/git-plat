# git-plat
A platform level multi-repo cloning system

git-plat.yaml
```yaml
master-folder-name: root # what subfolder to clone the git repo into
auto-symlink-to-master-files: true # will always create a .git-plat.yaml symlink
repos: 
  common: github.com:org/common.git
  infrastructure: github.com:org/infrastructure.git
  packages/x: github.com:org/x.git
  packages/y: github.com:org/y.git
  services/a: github.com:org/a.git
  services/b: github.com:org/b.git
  
repo-groups:
  subapp1: github.com:org/subapp1.git # this is just another git-plat repo
```
