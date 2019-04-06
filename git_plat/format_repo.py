def format_repo(repo: str, org, host, user):
    has_org = repo.find('/') != -1
    has_host = repo.find(':') != -1

    repo = repo if has_org else f'{org}/{repo}'
    repo = repo if has_host else f'{host or "github.com"}:{repo}'

    has_user = repo.find('@') != -1
    repo = repo if has_user else f'{user or git}@{repo}'
    return repo
