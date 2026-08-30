uv add snowflake-connector-python
Resolved 52 packages in 40ms
  × Failed to build `cryptography==50.0.1`
  ├─▶ The build backend returned an error
  ╰─▶ Call to `maturin.build_wheel` failed (exit status: 1)

      [stdout]
      cargo 1.98.0 (797e8a9bc 2026-08-05)
      Rust not found, installing into a temporary directory
      Running `maturin pep517 build-wheel -i
      /Users/aidanburke/rsm-msba/.rsm-msba/uv-cache/builds-v0/.tmpPKnvsd/bin/python
      --compatibility off`

      [stderr]
      Python reports SOABI: cpython-313-darwin
      Computed rustc target triple: x86_64-apple-darwin
      Installation directory:
      /Users/aidanburke/Library/Caches/puccinialin
      Rustup already downloaded
      Installing rust to
      /Users/aidanburke/Library/Caches/puccinialin/rustup
      warn: Rustup is not running natively. It's running under
      emulation of x86_64-apple-darwin.
      warn: For best compatibility and performance you should
      reinstall rustup for your native CPU.
      warn: It looks like you have an existing rustup settings file
      at:
      warn:
      /Users/aidanburke/Library/Caches/puccinialin/rustup/settings.toml
      warn: Rustup will install the default toolchain as specified in
      the settings file,
      warn: instead of the one inferred from the default host triple.
      info: profile set to minimal
      info: setting default host triple to x86_64-apple-darwin
      warn: Updating existing toolchain, profile choice will be
      ignored
      info: syncing channel updates for stable-x86_64-apple-darwin
      info: default toolchain set to stable-x86_64-apple-darwin
      Checking if cargo is installed
      🍹 Building a mixed python/rust project
      🐍 Found CPython 3.13 at
      /Users/aidanburke/rsm-msba/.rsm-msba/uv-cache/builds-v0/.tmpPKnvsd/bin/python
      🔗 Found pyo3 bindings with abi3 support
      📡 Using build options locked from pyproject.toml
         Compiling openssl-sys v0.9.117
         Compiling cryptography-x509 v0.50.1
      (/Users/aidanburke/rsm-msba/.rsm-msba/uv-cache/sdists-v9/pypi/cryptography/50.0.1/dbu4AfpN41YRJaSJ/src/src/rust/cryptography-x509)
         Compiling pyo3 v0.29.0
      warning: openssl-sys@0.9.117: Could not find directory of
      OpenSSL installation, and this `-sys` crate cannot proceed
      without this knowledge. If OpenSSL is installed and this
      crate had trouble finding it,  you can set the `OPENSSL_DIR`
      environment variable for the compilation process. See stderr
      section below for further information.
      error: failed to run custom build command for `openssl-sys
      v0.9.117`

      Caused by:
        process didn't exit successfully:
      `/Users/aidanburke/rsm-msba/.rsm-msba/uv-cache/sdists-v9/pypi/cryptography/50.0.1/dbu4AfpN41YRJaSJ/src/target/release/build/openssl-sys-6550a5fe5fc3548d/build-script-main`
      (exit status: 101)
        --- stdout
        cargo:rustc-check-cfg=cfg(osslconf, values("OPENSSL_NO_OCB",
      "OPENSSL_NO_SM4", "OPENSSL_NO_SEED", "OPENSSL_NO_CHACHA",
      "OPENSSL_NO_CAST", "OPENSSL_NO_IDEA", "OPENSSL_NO_CAMELLIA",
      "OPENSSL_NO_RC4", "OPENSSL_NO_BF", "OPENSSL_NO_PSK",
      "OPENSSL_NO_DEPRECATED_3_0", "OPENSSL_NO_SCRYPT",
      "OPENSSL_NO_SM3", "OPENSSL_NO_RMD160", "OPENSSL_NO_EC2M",
      "OPENSSL_NO_OCSP", "OPENSSL_NO_CMS", "OPENSSL_NO_COMP",
      "OPENSSL_NO_SOCK", "OPENSSL_NO_STDIO", "OPENSSL_NO_EC",
      "OPENSSL_NO_SSL3_METHOD", "OPENSSL_NO_KRB5",
      "OPENSSL_NO_TLSEXT", "OPENSSL_NO_SRP", "OPENSSL_NO_SRTP",
      "OPENSSL_NO_RFC3779", "OPENSSL_NO_SHA",
      "OPENSSL_NO_NEXTPROTONEG", "OPENSSL_NO_ENGINE",
      "OPENSSL_NO_BUF_FREELISTS", "OPENSSL_NO_RC2"))
        cargo:rustc-check-cfg=cfg(openssl)
        cargo:rustc-check-cfg=cfg(libressl)
        cargo:rustc-check-cfg=cfg(boringssl)
        cargo:rustc-check-cfg=cfg(awslc)
        cargo:rustc-check-cfg=cfg(awslc_pregenerated)
        cargo:rustc-check-cfg=cfg(libressl250)
        cargo:rustc-check-cfg=cfg(libressl251)
        cargo:rustc-check-cfg=cfg(libressl252)
        cargo:rustc-check-cfg=cfg(libressl261)
        cargo:rustc-check-cfg=cfg(libressl270)
        cargo:rustc-check-cfg=cfg(libressl271)
        cargo:rustc-check-cfg=cfg(libressl273)
        cargo:rustc-check-cfg=cfg(libressl280)
        cargo:rustc-check-cfg=cfg(libressl281)
        cargo:rustc-check-cfg=cfg(libressl291)
        cargo:rustc-check-cfg=cfg(libressl310)
        cargo:rustc-check-cfg=cfg(libressl321)
        cargo:rustc-check-cfg=cfg(libressl332)
        cargo:rustc-check-cfg=cfg(libressl340)
        cargo:rustc-check-cfg=cfg(libressl350)
        cargo:rustc-check-cfg=cfg(libressl360)
        cargo:rustc-check-cfg=cfg(libressl361)
        cargo:rustc-check-cfg=cfg(libressl370)
        cargo:rustc-check-cfg=cfg(libressl380)
        cargo:rustc-check-cfg=cfg(libressl381)
        cargo:rustc-check-cfg=cfg(libressl382)
        cargo:rustc-check-cfg=cfg(libressl390)
        cargo:rustc-check-cfg=cfg(libressl400)
        cargo:rustc-check-cfg=cfg(libressl410)
        cargo:rustc-check-cfg=cfg(libressl420)
        cargo:rustc-check-cfg=cfg(libressl430)
        cargo:rustc-check-cfg=cfg(ossl101)
        cargo:rustc-check-cfg=cfg(ossl102)
        cargo:rustc-check-cfg=cfg(ossl102f)
        cargo:rustc-check-cfg=cfg(ossl102h)
        cargo:rustc-check-cfg=cfg(ossl110)
        cargo:rustc-check-cfg=cfg(ossl110f)
        cargo:rustc-check-cfg=cfg(ossl110g)
        cargo:rustc-check-cfg=cfg(ossl110h)
        cargo:rustc-check-cfg=cfg(ossl111)
        cargo:rustc-check-cfg=cfg(ossl111b)
        cargo:rustc-check-cfg=cfg(ossl111c)
        cargo:rustc-check-cfg=cfg(ossl111d)
        cargo:rustc-check-cfg=cfg(ossl300)
        cargo:rustc-check-cfg=cfg(ossl310)
        cargo:rustc-check-cfg=cfg(ossl320)
        cargo:rustc-check-cfg=cfg(ossl330)
        cargo:rustc-check-cfg=cfg(ossl340)
        cargo:rustc-check-cfg=cfg(ossl400)
        cargo:rerun-if-env-changed=X86_64_APPLE_DARWIN_OPENSSL_LIB_DIR
        X86_64_APPLE_DARWIN_OPENSSL_LIB_DIR unset
        cargo:rerun-if-env-changed=OPENSSL_LIB_DIR
        OPENSSL_LIB_DIR unset
        cargo:rerun-if-env-changed=X86_64_APPLE_DARWIN_OPENSSL_INCLUDE_DIR
        X86_64_APPLE_DARWIN_OPENSSL_INCLUDE_DIR unset
        cargo:rerun-if-env-changed=OPENSSL_INCLUDE_DIR
        OPENSSL_INCLUDE_DIR unset
        cargo:rerun-if-env-changed=X86_64_APPLE_DARWIN_OPENSSL_DIR
        X86_64_APPLE_DARWIN_OPENSSL_DIR unset
        cargo:rerun-if-env-changed=OPENSSL_DIR
        OPENSSL_DIR unset
        cargo:rerun-if-env-changed=OPENSSL_NO_PKG_CONFIG
        cargo:rerun-if-env-changed=PKG_CONFIG_x86_64-apple-darwin
        cargo:rerun-if-env-changed=PKG_CONFIG_x86_64_apple_darwin
        cargo:rerun-if-env-changed=HOST_PKG_CONFIG
        cargo:rerun-if-env-changed=PKG_CONFIG
        cargo:rerun-if-env-changed=OPENSSL_STATIC
        cargo:rerun-if-env-changed=OPENSSL_DYNAMIC
        cargo:rerun-if-env-changed=PKG_CONFIG_ALL_STATIC
        cargo:rerun-if-env-changed=PKG_CONFIG_ALL_DYNAMIC
        cargo:rerun-if-env-changed=PKG_CONFIG_PATH_x86_64-apple-darwin
        cargo:rerun-if-env-changed=PKG_CONFIG_PATH_x86_64_apple_darwin
        cargo:rerun-if-env-changed=HOST_PKG_CONFIG_PATH
        cargo:rerun-if-env-changed=PKG_CONFIG_PATH
        cargo:rerun-if-env-changed=PKG_CONFIG_LIBDIR_x86_64-apple-darwin
        cargo:rerun-if-env-changed=PKG_CONFIG_LIBDIR_x86_64_apple_darwin
        cargo:rerun-if-env-changed=HOST_PKG_CONFIG_LIBDIR
        cargo:rerun-if-env-changed=PKG_CONFIG_LIBDIR
        cargo:rerun-if-env-changed=PKG_CONFIG_SYSROOT_DIR_x86_64-apple-darwin
        cargo:rerun-if-env-changed=PKG_CONFIG_SYSROOT_DIR_x86_64_apple_darwin
        cargo:rerun-if-env-changed=HOST_PKG_CONFIG_SYSROOT_DIR
        cargo:rerun-if-env-changed=PKG_CONFIG_SYSROOT_DIR
        cargo:rerun-if-env-changed=OPENSSL_STATIC
        cargo:rerun-if-env-changed=OPENSSL_DYNAMIC
        cargo:rerun-if-env-changed=PKG_CONFIG_ALL_STATIC
        cargo:rerun-if-env-changed=PKG_CONFIG_ALL_DYNAMIC
        cargo:rerun-if-env-changed=PKG_CONFIG_PATH_x86_64-apple-darwin
        cargo:rerun-if-env-changed=PKG_CONFIG_PATH_x86_64_apple_darwin
        cargo:rerun-if-env-changed=HOST_PKG_CONFIG_PATH
        cargo:rerun-if-env-changed=PKG_CONFIG_PATH
        cargo:rerun-if-env-changed=PKG_CONFIG_LIBDIR_x86_64-apple-darwin
        cargo:rerun-if-env-changed=PKG_CONFIG_LIBDIR_x86_64_apple_darwin
        cargo:rerun-if-env-changed=HOST_PKG_CONFIG_LIBDIR
        cargo:rerun-if-env-changed=PKG_CONFIG_LIBDIR
        cargo:rerun-if-env-changed=PKG_CONFIG_SYSROOT_DIR_x86_64-apple-darwin
        cargo:rerun-if-env-changed=PKG_CONFIG_SYSROOT_DIR_x86_64_apple_darwin
        cargo:rerun-if-env-changed=HOST_PKG_CONFIG_SYSROOT_DIR
        cargo:rerun-if-env-changed=PKG_CONFIG_SYSROOT_DIR


        Could not find openssl via pkg-config:
        Could not run `PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1 pkg-config
      --libs --cflags openssl`
        The pkg-config command could not be found.

        Most likely, you need to install a pkg-config package for
      your OS.
        Try `brew install pkgconf` if you have Homebrew.

        If you've already installed it, ensure the pkg-config command
      is one of the
        directories in the PATH environment variable.

        If you did not expect this build to link to a pre-installed
      system library,
        then check documentation of the openssl-sys crate for an
      option to
        build the library from source, or disable features or
      dependencies
        that require pkg-config.

        cargo:warning=Could not find directory of OpenSSL
      installation, and this `-sys` crate cannot proceed without this
      knowledge. If OpenSSL is installed and this crate had trouble
      finding it,  you can set the `OPENSSL_DIR` environment variable
      for the compilation process. See stderr section below for
      further information.

        --- stderr


        Could not find directory of OpenSSL installation, and this
      `-sys` crate cannot
        proceed without this knowledge. If OpenSSL is installed and
      this crate had
        trouble finding it,  you can set the `OPENSSL_DIR` environment
      variable for the
        compilation process.

        Make sure you also have the development packages of openssl
      installed.
        For example, `libssl-dev` on Ubuntu or `openssl-devel` on
      Fedora.

        If you're in a situation where you think the directory
      *should* be found
        automatically, please open a bug at
      https://github.com/rust-openssl/rust-openssl
        and include information about your system as well as this
      message.

        $HOST = x86_64-apple-darwin
        $TARGET = x86_64-apple-darwin
        openssl-sys = 0.9.117


      warning: build failed, waiting for other jobs to finish...
      💥 maturin failed
        Caused by: Failed to build a native library through cargo
        Caused by: Cargo build finished
      with "exit status: 101": `env -u CARGO
      CARGO_ENCODED_RUSTFLAGS="-C\u{1f}link-arg=-undefined\u{1f}-C\u{1f}link-arg=dynamic_lookup"
      PYO3_BUILD_EXTENSION_MODULE="1"
      PYO3_CONFIG_FILE="/Users/aidanburke/rsm-msba/.rsm-msba/uv-cache/sdists-v9/pypi/cryptography/50.0.1/dbu4AfpN41YRJaSJ/src/target/maturin/pyo3-config-x86_64-apple-darwin-3.13-abi3.txt"
      PYO3_ENVIRONMENT_SIGNATURE="cpython-3.13-64bit"
      PYO3_PYTHON="/Users/aidanburke/rsm-msba/.rsm-msba/uv-cache/builds-v0/.tmpPKnvsd/bin/python"
      PYTHON_SYS_EXECUTABLE="/Users/aidanburke/rsm-msba/.rsm-msba/uv-cache/builds-v0/.tmpPKnvsd/bin/python"
      "cargo" "rustc" "--profile" "release" "--message-format"
      "json-render-diagnostics" "--locked" "--manifest-path"
      "/Users/aidanburke/rsm-msba/.rsm-msba/uv-cache/sdists-v9/pypi/cryptography/50.0.1/dbu4AfpN41YRJaSJ/src/src/rust/Cargo.toml"
      "--lib" "--" "-C"
      "link-args=-Wl,-install_name,@rpath/cryptography.hazmat.bindings._rust.abi3.so"`
      Error: command ['maturin', 'pep517', 'build-wheel', '-i',
      '/Users/aidanburke/rsm-msba/.rsm-msba/uv-cache/builds-v0/.tmpPKnvsd/bin/python',
      '--compatibility', 'off'] returned non-zero exit status 1


hint: `cryptography` (v50.0.1) was included because `snowflake` (v0.1.0) depends on `snowflake-connector-python` (v4.7.2) which depends on `cryptography`
hint: Build failures usually indicate a problem with the package or the build environment
hint: If you want to add the package regardless of the failed resolution, provide the `--frozen` flag to skip locking and syncing%              direnv: loading ~/rsm-msba/mgta464/snowflake/.envrc
direnv: loading ~/rsm-msba/mgta464/.envrc
direnv: loading ~/rsm-msba/.envrc
direnv: using flake /Users/aidanburke/rsm-nix
direnv: nix-direnv: Using cached dev shell
===================================================
 RSM-MSBA computing environment (Nix flake)
   workspace : /Users/aidanburke/rsm-msba
   state     : /Users/aidanburke/rsm-msba/.rsm-msba
   python    : /Users/aidanburke/rsm-msba/.rsm-msba/envs/nix-uv
   db        : rsm-pg-start | rsm-pg-psql | rsm-pgweb
===================================================
direnv: export +AR +AS +CC +CONFIG_SHELL +CXX +DETERMINISTIC_BUILD +DEVELOPER_DIR +DYLD_FALLBACK_LIBRARY_PATH +HOST_PATH +IN_NIX_SHELL +JUPYTER_DATA_DIR +JUPYTER_PATH +LD +LD_DYLD_PATH +MACOSX_DEPLOYMENT_TARGET +NIX_APPLE_SDK_VERSION +NIX_BINTOOLS +NIX_BINTOOLS_WRAPPER_TARGET_HOST_arm64_apple_darwin +NIX_BUILD_CORES +NIX_CC +NIX_CC_WRAPPER_TARGET_HOST_arm64_apple_darwin +NIX_CFLAGS_COMPILE +NIX_DONT_SET_RPATH +NIX_DONT_SET_RPATH_FOR_BUILD +NIX_ENFORCE_NO_NATIVE +NIX_HARDENING_ENABLE +NIX_IGNORE_LD_THROUGH_GCC +NIX_LDFLAGS +NIX_NO_SELF_RPATH +NIX_STORE +NM +NPM_CONFIG_CACHE +NPM_CONFIG_PREFIX +OBJCOPY +OBJDUMP +PATH_LOCALE +PGDATA +PGDATABASE +PGHOST +PGPORT +PGUSER +PGWEB_PORT +PYTHONHASHSEED +PYTHONNOUSERSITE +PYTHONPATH +QUARTO_PYTHON +RANLIB +RSMBASE +RSM_BANNER_SHOWN +RSM_FLAKE +RSM_OMP_LIBDIR +RSM_UV_ENV +RSM_WORKSPACE +SDKROOT +SIZE +SOURCE_DATE_EPOCH +SSL_CERT_FILE +STRINGS +STRIP +SYSTEM_CERTIFICATE_PATH +UV_CACHE_DIR +UV_LINK_MODE +UV_PROJECT_ENVIRONMENT +UV_PYTHON_PREFERENCE +VIRTUAL_ENV +VIRTUAL_ENV_PROMPT +ZERO_AR_DATE +__darwinAllowLocalNetworking +__impureHostDeps +__propagatedImpureHostDeps +__propagatedSandboxProfile +__sandboxProfile +__structuredAttrs +buildInputs +buildPhase +builder +cmakeFlags +configureFlags +depsBuildBuild +depsBuildBuildPropagated +depsBuildTarget +depsBuildTargetPropagated +depsHostHost +depsHostHostPropagated +depsTargetTarget +depsTargetTargetPropagated +doCheck +doInstallCheck +dontAddDisableDepTrack +mesonFlags +name +nativeBuildInputs +out +outputs +patches +phases +preferLocalBuild +propagatedBuildInputs +propagatedNativeBuildInputs +shell +shellHook +stdenv +strictDeps +system ~NIX_SSL_CERT_FILE ~PATH ~XDG_DATA_DIRS ~XPC_SERVICE_NAME
