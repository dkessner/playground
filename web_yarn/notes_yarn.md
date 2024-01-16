# Notes on Javascript, yarn and webpack

## Initialize

Add `yarn` to `PATH`:

```console
corepack enable
```

Initialize project with Yarn v2:

```console
yarn init -2
```

Update yarn:

```console
yarn set version stable
yarn install
```

## Install packages

Add `webpack` as dev dependency:

```console
yarn add webpack --dev
```

Add `lodash`:

```console
yarn add lodash --dev
```

## Project structure

- package.json
- yarn.lock
- src
    - index.js
- dist
    - index.html

## Build

This works with warnings:
```console
yarn webpack
```

Set `mode` to prevent warnings:

```console
yarn webpack --mode=development
yarn webpack --mode=production
```

This is the recommended command from the 
[webpack Getting Started guide](https://webpack.js.org/guides/getting-started/),
but gave errors:

```console
npx webpack
```




