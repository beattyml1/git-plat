# git-plat
A platform level multi-repo cloning system

git-plat.yaml
```yaml
master-folder-name: root # what subfolder to clone the git repo into
auto-symlink-to-master-files: true # will always create a .git-plat.yaml symlink
git-host: github.com
git-org: org

repos: 
  common: git@github.com:org/common.git # defaults remote name to origin
  infrastructure: infrastructure
  packages/x: x
  packages/y: 
    origin: b
    gemfury: git@gemfury.com:org/common.git 
    # you can always add more remotes in the repo, this is for shared remotes
    # that way when the new hire shows up they are ready to go with all remotes
  services/a: a
  services/b: 
    origin: b
    heroku: git@heroku.com:org/common.git
  
repo-groups:
  subapp1: git@github.com:child-org/subapp1.git # this is just another git-plat repo
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

Init
```
git-plat init packages/z    : will create new repo called z in packages, add to registry, and add remote
git-plat init zz packages/z    : will create new repo called zz on the remote at packages/z, add to registry, and add remote
```

Right now we're not focused on committing, status, and history logs as a group since it's often a sign you should just use a mono repo
