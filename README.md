# DevRestrictedArea

Small Project Set

---

## New Submodules

```
git submodule add MYURL
```

## Push

```
git push --recurse-submodules=on-demand
```

## Clone

1. All Project Clone

```
git clone --recursive https://github.com/lastone9182/DevRestrictArea.git
```

2. If skip `--recursive` option

```
git clone https://github.com/lastone9182/DevRestrictArea.git

git submodule update --init --recursive
```

3. Update specific submodules

```
# DevRestrictArea directory
git submodule update --remote PROJECT

# in submodule directory
git fetch
```