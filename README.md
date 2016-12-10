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

- All Project Clone

```
git clone --recursive https://github.com/lastone9182/RestrictZone.git
```

- If skip `--recursive` option

```
git clone https://github.com/lastone9182/RestrictZone.git

git submodule update --init --recursive
```

- Update specific submodules

```
# DevRestrictArea directory
git submodule update --remote PROJECT

# in submodule directory
git fetch
```