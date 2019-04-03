# git-plat
A platform level multi-repo cloning system

git-plat.yaml
```yaml
master-folder-name: root # what subfolder to clone the git repo into
auto-symlink-to-master-files: true # will always create a .git-plat.yaml symlink
repos: 
  common: git@github.com:org/common.git
  infrastructure: git@github.com:org/infrastructure.git
  packages/x: git@github.com:org/x.git
  packages/y: git@github.com:org/y.git
  services/a: git@github.com:org/a.git
  services/b: git@github.com:org/b.git
  
repo-groups:
  subapp1: github.com:org/subapp1.git # this is just another git-plat repo
```


Clone a repo group
```
git-plat clone git@github.com:org/root.git            : just the base
git-plat clone children git@github.com:org/root.git   : and direct children 
git-plat clone ancestors git@github.com:org/root.git  : all ancestors
```

Clone children/ancestors
```
git-plat clone children   : direct children 
git-plat clone ancestors  : all ancestors
```

Fetch changes
```
git-plat fetch            : platform and children direct children 
git-plat fetch ancestors  : all ancestors
```

Pull changes
```
git-plat pull children origin master  : git pull origin master on all direct children
git-plat pull ancestors origin master  : all ancestors
git-plat pull x origin master       : pulls the repo called x, only works if uniquely named
git-plat pull packages/x origin master : pulls the repo at path packages/x 
```

Right now we're not focused on committing, status, and history logs as a group since it's often a sign you should just use a mono repo
