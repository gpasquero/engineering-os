# Vendored dependencies

**Engineering OS ships one third-party library so that using it requires no
installation step at all.**

## `yaml/` — PyYAML

- **Upstream:** https://pyyaml.org · https://github.com/yaml/pyyaml
- **Licence:** MIT (see `yaml/LICENSE`), compatible with Apache-2.0
- **What was changed:** the optional `libyaml` C extension binding (`cyaml.py`)
  is not vendored, so the copy here is **pure Python** and works on any
  interpreter without a compiler or a wheel.

Engineering OS uses exactly two functions from it — `safe_load` and
`safe_dump`. Writing a small YAML subset parser instead was considered and
rejected: this repository has already lost two sessions to YAML edge cases
(a title beginning with `"`, a list item beginning with `*`), and a hand-rolled
parser would reintroduce that class of defect in the one place where a silent
misparse is most expensive.

An installed PyYAML always wins: `vendor/` is appended to `sys.path`, never
prepended.
