# Changelog

This document describes changes to the public interfaces in the Amaranth language and standard library. It does not include most bug fixes or implementation changes; versions which do not include notable changes are not listed here.

## Documentation for past releases

Documentation for past releases of the Amaranth language and toolchain is available online:

- [Amaranth 0.5.0](https://amaranth-lang.org/docs/amaranth/v0.5.0/)
- [Amaranth 0.4.5](https://amaranth-lang.org/docs/amaranth/v0.4.5/)
- [Amaranth 0.4.4](https://amaranth-lang.org/docs/amaranth/v0.4.4/)
- [Amaranth 0.4.3](https://amaranth-lang.org/docs/amaranth/v0.4.3/)
- [Amaranth 0.4.2](https://amaranth-lang.org/docs/amaranth/v0.4.2/)
- [Amaranth 0.4.1](https://amaranth-lang.org/docs/amaranth/v0.4.1/)
- [Amaranth 0.4.0](https://amaranth-lang.org/docs/amaranth/v0.4.0/)
- [Amaranth 0.3](https://amaranth-lang.org/docs/amaranth/v0.3/)

## Version 0.6.0 (unreleased)

### Implemented RFCs

- [RFC 66]: Simulation time
- [RFC 71]: `EnumView.matches`

### Language changes

- Added: [`Period`][amaranth.hdl.Period] for representing time periods. ([RFC 66])
- Changed: overriding [`ValueCastable.from_bits`][amaranth.hdl.ValueCastable.from_bits] is now mandatory. ([RFC 51])
- Deprecated: the `#!python local=` argument to [`ClockDomain`][amaranth.hdl.ClockDomain]. ([RFC 59])
- Removed: (deprecated in 0.4.0) [`Record`][amaranth.hdl.Record].
- Removed: (deprecated in 0.5.0) [`Memory`][amaranth.hdl.Memory] ([RFC 45])
- Removed: (deprecated in 0.5.0) public submodules of [`amaranth.hdl`][amaranth.hdl].
- Removed: (deprecated in 0.5.0) [`Value.implies`][amaranth.hdl.Value.implies].
- Removed: (deprecated in 0.5.0) [`Const.width`][amaranth.hdl.Const.width], [`Const.signed`][amaranth.hdl.Const.signed], [`Signal.width`][amaranth.hdl.Signal.width], [`Signal.signed`][amaranth.hdl.Signal.signed].
- Removed: (deprecated in 0.5.0) upwards propagation of clock domains. ([RFC 59])
- Removed: (deprecated in 0.5.0) [`amaranth.utils.log2_int`][amaranth.utils.log2_int]. ([RFC 17])

### Standard library changes

- Added: `#!python payload_init=` argument in [`amaranth.lib.stream.Signature`][amaranth.lib.stream.Signature].
- Added: [`enum.EnumView.matches`][amaranth.lib.enum.EnumView.matches]. ([RFC 71])
- Changed: (deprecated in 0.5.1) providing [`io.PortLike.__add__`][amaranth.lib.io.PortLike.__add__] is now mandatory. ([RFC 69])
- Removed: (deprecated in 0.5.0) [`amaranth.lib.coding`][amaranth.lib.coding]. ([RFC 63])

### Toolchain changes

- Added: [`SimulatorContext.elapsed_time`][amaranth.sim._async.SimulatorContext.elapsed_time] for getting elapsed simulation time. ([RFC 66])
- Added: [`Platform.default_clk_period`][amaranth.build.plat.Platform.default_clk_period]. ([RFC 66])
- Changed: [`Simulator.add_clock`][amaranth.sim.Simulator.add_clock] now accepts a [`Period`][amaranth.hdl.Period] for `#!python period` and `#!python phase`. ([RFC 66])
- Changed: [`Simulator.run_until`][amaranth.sim.Simulator.run_until] now accepts a [`Period`][amaranth.hdl.Period] for `#!python deadline`. ([RFC 66])
- Changed: [`SimulatorContext.delay`][amaranth.sim._async.SimulatorContext.delay] now accepts a [`Period`][amaranth.hdl.Period] for `#!python interval`. ([RFC 66])
- Changed: [`ResourceManager.add_clock_constraint`][amaranth.build.res.ResourceManager.add_clock_constraint] now accepts a [`Period`][amaranth.hdl.Period] for `#!python period`. ([RFC 66])
- Changed: [`Clock`][amaranth.build.dsl.Clock] now accepts a [`Period`][amaranth.hdl.Period] for `#!python period`. ([RFC 66])
- Changed: [`Clock.period`][amaranth.build.dsl.Clock.period] now returns a [`Period`][amaranth.hdl.Period]. ([RFC 66])
- Deprecated: Passing a [`float`][amaranth.lib.float] of seconds or hertz to any of the methods/arguments now accepting a [`Period`][amaranth.hdl.Period]. ([RFC 66])
- Deprecated: Passing `#!python frequency=` to [`ResourceManager.add_clock_constraint`][amaranth.build.res.ResourceManager.add_clock_constraint]. ([RFC 66])
- Deprecated: Passing `#!python frequency=` to [`Clock`][amaranth.build.dsl.Clock]. ([RFC 66])
- Deprecated: [`Clock.frequency`][amaranth.build.dsl.Clock.frequency]. ([RFC 66])
- Deprecated: [`Platform.default_clk_frequency`][amaranth.build.plat.Platform.default_clk_frequency]. ([RFC 66])

### Platform integration changes

- Changed: the Gowin platform now uses `nextpnr-himbaechel` rather than `nextpnr-gowin`.

## Version 0.5.3 (unreleased)

### Language changes

- Added: individual bits of the same signal can now be assigned from different modules or domains.

## Version 0.5.2

### Standard library changes

- Added: constants of [`amaranth.lib.data.ArrayLayout`][amaranth.lib.data.ArrayLayout] can be indexed with negative integers or slices.
- Added: `#!python len()` works on constants of [`amaranth.lib.data.ArrayLayout`][amaranth.lib.data.ArrayLayout].
- Added: constants of [`amaranth.lib.data.ArrayLayout`][amaranth.lib.data.ArrayLayout] are iterable.

### Platform integration changes

- Added: [`Platform.request`][amaranth.vendor.Platform.request] accepts `#!python dir="-"` for resources with subsignals.

## Version 0.5.1

### Implemented RFCs

- [RFC 69]: Add a `lib.io.PortLike` object usable in simulation

### Standard library changes

- Added: views of [`amaranth.lib.data.ArrayLayout`][amaranth.lib.data.ArrayLayout] can be indexed with negative integers or slices.
- Added: `#!python len()` works on views of [`amaranth.lib.data.ArrayLayout`][amaranth.lib.data.ArrayLayout].
- Added: views of [`amaranth.lib.data.ArrayLayout`][amaranth.lib.data.ArrayLayout] are iterable.
- Added: [`io.SimulationPort`][amaranth.lib.io.SimulationPort]. ([RFC 69])

## Version 0.5.0

The Migen compatibility layer has been removed.

### Migrating from version 0.4

Apply the following changes to code written against Amaranth 0.4 to migrate it to version 0.5:

- Update uses of `#!python reset=` keyword argument to `#!python init=`.
- Ensure all elaboratables are subclasses of [`Elaboratable`][amaranth.lib.Elaboratable].
- Replace uses of `#!python m.Case()` with no patterns with `#!python m.Default()`.
- Replace uses of `#!python Value.matches()` with no patterns with `#!python Const(1)`.
- Ensure clock domains aren't used outside the module that defines them, or its submodules; move clock domain definitions upwards in the hierarchy as necessary
- Replace imports of `#!python amaranth.asserts.Assert`, `#!python Assume`, and `#!python Cover` with imports from `#!python amaranth.hdl`.
- Remove uses of `#!python name=` keyword argument of `#!python Assert`, `#!python Assume`, and `#!python Cover`; a message can be used instead.
- Replace uses of `#!python amaranth.hdl.Memory` with [`amaranth.lib.memory.Memory`][amaranth.lib.memory.Memory].
- Update uses of `#!python platform.request` to pass `#!python dir="-"` and use [`amaranth.lib.io`][amaranth.lib.io] buffers.
- Remove uses of `#!python amaranth.lib.coding.*` by inlining or copying the implementation of the modules.
- Convert uses of `#!python Simulator.add_sync_process` used as testbenches to [`Simulator.add_testbench`][amaranth.sim.Simulator.add_testbench].
- Convert other uses of `#!python Simulator.add_sync_process` to [`Simulator.add_process`][amaranth.sim.Simulator.add_process].
- Convert simulator processes and testbenches to use the new async API.
- Update uses of [`Simulator.add_clock`][amaranth.sim.Simulator.add_clock] with explicit `#!python phase` to take into account simulator no longer adding implicit `#!python period / 2`. (Previously, [`Simulator.add_clock`][amaranth.sim.Simulator.add_clock] was documented to first toggle the clock at the time `#!python phase`, but actually first toggled the clock at `#!python period / 2 + phase`.)
- Update uses of [`Simulator.run_until`][amaranth.sim.Simulator.run_until] to remove the `#!python run_passive=True` argument. If the code uses `#!python run_passive=False`, ensure it still works with the new behavior.
- Update uses of `#!python amaranth.utils.log2_int(need_pow2=False)` to [`amaranth.utils.ceil_log2`][amaranth.utils.ceil_log2].
- Update uses of `#!python amaranth.utils.log2_int(need_pow2=True)` to [`amaranth.utils.exact_log2`][amaranth.utils.exact_log2].
- Replace uses of `#!python a.implies(b)` with `~a | b`.

### Implemented RFCs

- [RFC 17]: Remove `log2_int`
- [RFC 27]: Testbench processes for the simulator
- [RFC 30]: Component metadata
- [RFC 36]: Async testbench functions
- [RFC 39]: Change semantics of no-argument `m.Case()`
- [RFC 42]: `Const` from shape-castable
- [RFC 43]: Rename `reset=` to `init=`
- [RFC 45]: Move `hdl.Memory` to `lib.Memory`
- [RFC 46]: Change `Shape.cast(range(1))` to `unsigned(0)`
- [RFC 50]: `Print` statement and string formatting
- [RFC 51]: Add `ShapeCastable.from_bits` and `amaranth.lib.data.Const`
- [RFC 53]: Low-level I/O primitives
- [RFC 55]: New `lib.io` components
- [RFC 58]: Core support for `ValueCastable` formatting
- [RFC 59]: Get rid of upwards propagation of clock domains
- [RFC 61]: Minimal streams
- [RFC 62]: The `MemoryData` class
- [RFC 63]: Remove `amaranth.lib.coding`
- [RFC 65]: Special formatting for structures and enums

### Language changes

- Added: [`Slice`][amaranth.hdl.Slice] objects have been made const-castable.
- Added: [`amaranth.utils.ceil_log2`][amaranth.utils.ceil_log2], [`amaranth.utils.exact_log2`][amaranth.utils.exact_log2]. ([RFC 17])
- Added: [`Format`][amaranth.hdl.Format] objects, [`Print`][amaranth.hdl.Print] statements, messages in [`Assert`][amaranth.hdl.Assert], [`Assume`][amaranth.hdl.Assume] and [`Cover`][amaranth.hdl.Cover]. ([RFC 50])
- Added: [`ShapeCastable.from_bits`][amaranth.hdl.ShapeCastable.from_bits] method. ([RFC 51])
- Added: IO values, [`IOPort`][amaranth.hdl.IOPort] objects, [`IOBufferInstance`][amaranth.hdl.IOBufferInstance] objects. ([RFC 53])
- Added: [`MemoryData`][amaranth.hdl.MemoryData] objects. ([RFC 62])
- Changed: `#!python m.Case()` with no patterns is never active instead of always active. ([RFC 39])
- Changed: `#!python Value.matches()` with no patterns is `#!python Const(0)` instead of `#!python Const(1)`. ([RFC 39])
- Changed: `#!python Signal(range(stop), init=stop)` warning has been changed into a hard error and made to trigger on any out-of range value.
- Changed: `#!python Signal(range(0))` is now valid without a warning.
- Changed: `#!python Const(value, shape)` now accepts shape-castable objects as `#!python shape`. ([RFC 42])
- Changed: `#!python Shape.cast(range(1))` is now `#!python unsigned(0)`. ([RFC 46])
- Changed: the `#!python reset=` argument of [`Signal`][amaranth.hdl.Signal], [`Signal.like`][amaranth.hdl.Signal.like], [`amaranth.lib.wiring.Member`][amaranth.lib.wiring.Member], [`amaranth.lib.cdc.FFSynchronizer`][amaranth.lib.cdc.FFSynchronizer], and `#!python m.FSM()` has been renamed to `#!python init=`. ([RFC 43])
- Changed: [`Shape`][amaranth.hdl.Shape] has been made immutable and hashable.
- Changed: [`Assert`][amaranth.hdl.Assert], [`Assume`][amaranth.hdl.Assume], [`Cover`][amaranth.hdl.Cover] have been moved to [`amaranth.hdl`][amaranth.hdl] from [`amaranth.asserts`][amaranth.asserts]. ([RFC 50])
- Changed: [`Instance`][amaranth.hdl.Instance] IO ports now accept only IO values, not plain values. ([RFC 53])
- Deprecated: [`amaranth.utils.log2_int`][amaranth.utils.log2_int]. ([RFC 17])
- Deprecated: [`amaranth.hdl.Memory`][amaranth.hdl.Memory]. ([RFC 45])
- Deprecated: upwards propagation of clock domains. ([RFC 59])
- Deprecated: [`Value.implies`][amaranth.hdl.Value.implies].
- Removed: (deprecated in 0.4.0) [`Const.normalize`][amaranth.hdl.Const.normalize]. ([RFC 5])
- Removed: (deprecated in 0.4.0) [`Repl`][amaranth.hdl.Repl]. ([RFC 10])
- Removed: (deprecated in 0.4.0) [`ast.Sample`][amaranth.hdl.ast.Sample], [`ast.Past`][amaranth.hdl.ast.Past], [`ast.Stable`][amaranth.hdl.ast.Stable], [`ast.Rose`][amaranth.hdl.ast.Rose], [`ast.Fell`][amaranth.hdl.ast.Fell].
- Removed: assertion names in [`Assert`][amaranth.hdl.Assert], [`Assume`][amaranth.hdl.Assume] and [`Cover`][amaranth.hdl.Cover]. ([RFC 50])
- Removed: accepting non-subclasses of [`Elaboratable`][amaranth.hdl.Elaboratable] as elaboratables.

### Standard library changes

- Added: [`amaranth.lib.memory`][amaranth.lib.memory]. ([RFC 45])
- Added: [`amaranth.lib.data.Const`][amaranth.lib.data.Const] class. ([RFC 51])
- Changed: [`amaranth.lib.data.Layout.const`][amaranth.lib.data.Layout.const] returns a [`amaranth.lib.data.Const`][amaranth.lib.data.Const], not a view ([RFC 51])
- Changed: [`amaranth.lib.wiring.Signature.is_compliant`][amaranth.lib.wiring.Signature.is_compliant] no longer rejects reset-less signals.
- Added: [`amaranth.lib.io.SingleEndedPort`][amaranth.lib.io.SingleEndedPort], [`amaranth.lib.io.DifferentialPort`][amaranth.lib.io.DifferentialPort]. ([RFC 55])
- Added: [`amaranth.lib.io.Buffer`][amaranth.lib.io.Buffer], [`amaranth.lib.io.FFBuffer`][amaranth.lib.io.FFBuffer], [`amaranth.lib.io.DDRBuffer`][amaranth.lib.io.DDRBuffer]. ([RFC 55])
- Added: [`amaranth.lib.meta`][amaranth.lib.meta], [`amaranth.lib.wiring.ComponentMetadata`][amaranth.lib.wiring.ComponentMetadata]. ([RFC 30])
- Added: [`amaranth.lib.stream`][amaranth.lib.stream]. ([RFC 61])
- Deprecated: [`amaranth.lib.coding`][amaranth.lib.coding]. ([RFC 63])
- Removed: (deprecated in 0.4.0) [`amaranth.lib.scheduler`][amaranth.lib.scheduler]. ([RFC 19])
- Removed: (deprecated in 0.4.0) [`amaranth.lib.fifo.FIFOInterface`][amaranth.lib.fifo.FIFOInterface] with `#!python fwft=False`. ([RFC 20])
- Removed: (deprecated in 0.4.0) [`amaranth.lib.fifo.SyncFIFO`][amaranth.lib.fifo.SyncFIFO] with `#!python fwft=False`. ([RFC 20])

### Toolchain changes

- Added: [`Simulator.add_testbench`][amaranth.sim.Simulator.add_testbench]. ([RFC 27])
- Added: async function support in [`Simulator.add_testbench`][amaranth.sim.Simulator.add_testbench] and [`Simulator.add_process`][amaranth.sim.Simulator.add_process]. ([RFC 36])
- Added: support for [`amaranth.hdl.Assert`][amaranth.hdl.Assert] in simulation. ([RFC 50])
- Changed: [`Simulator.add_clock`][amaranth.sim.Simulator.add_clock] no longer implicitly adds `#!python period / 2` when `#!python phase` is specified, actually matching the documentation.
- Changed: [`Simulator.run_until`][amaranth.sim.Simulator.run_until] always runs the simulation until the given deadline, even when no critical processes or testbenches are present.
- Deprecated: `#!python Settle` simulation command. ([RFC 27])
- Deprecated: `#!python Simulator.add_sync_process`. ([RFC 27])
- Deprecated: generator-based simulation processes and testbenches. ([RFC 36])
- Deprecated: the `#!python run_passive` argument to [`Simulator.run_until`][amaranth.sim.Simulator.run_until] has been deprecated, and does nothing.
- Removed: (deprecated in 0.4.0) use of mixed-case toolchain environment variable names, such as `NMIGEN_ENV_Diamond` or `AMARANTH_ENV_Diamond`; use upper-case environment variable names, such as `AMARANTH_ENV_DIAMOND`.

### Platform integration changes

- Added: [`BuildPlan.execute_local_docker`][amaranth.vendor.BuildPlan.execute_local_docker].
- Added: [`BuildPlan.extract`][amaranth.vendor.BuildPlan.extract].
- Added: `build.sh`  begins with `#!/bin/sh`.
- Changed: `IntelPlatform` renamed to `AlteraPlatform`.
- Deprecated: argument `#!python run_script=` in [`BuildPlan.execute_local`][amaranth.vendor.BuildPlan.execute_local].
- Removed: (deprecated in 0.4.0) [`vendor.intel`][vendor.intel], [`vendor.lattice_ecp5`][vendor.lattice_ecp5], [`vendor.lattice_ice40`][vendor.lattice_ice40], [`vendor.lattice_machxo2_3l`][vendor.lattice_machxo2_3l], [`vendor.quicklogic`][vendor.quicklogic], [`vendor.xilinx`][vendor.xilinx]. ([RFC 18])

## Version 0.4.0

Support has been added for a new and improved way of defining data structures in [`amaranth.lib.data`][amaranth.lib.data] and component interfaces in [`amaranth.lib.wiring`][amaranth.lib.wiring], as defined in [RFC 1] and [RFC 2]. [`Record`][amaranth.vendor.Record] has been deprecated. In a departure from the usual policy, to give designers additional time to migrate, [`Record`][amaranth.vendor.Record] will be removed in Amaranth 0.6 (one release later than normal).

Support for enumerations has been extended. A shape for enumeration members can be provided for an enumeration class, as defined in [RFC 3].

The language includes several new extension points for integration with [`Value`][amaranth.vendor.Value] based data structures defined outside of the core language. In particular, `Signal(shape)` may now return a [`Signal`][amaranth.vendor.Signal] object wrapped in another if `shape` implements the call protocol, as defined in [RFC 15].

Several issues with shape inference have been resolved. Notably, `a - b` where both `a` and `b` are unsigned now returns a signed value.

Support for Python 3.6 and 3.7 has been removed, and support for Python 3.11 and 3.12 has been added.

Features deprecated in version 0.3 have been removed. In particular, the `nmigen.*` namespace is not provided, `# nmigen:` annotations are not recognized, and `NMIGEN_*` envronment variables are not used.

The Migen compatibility layer remains deprecated (as it had been since Amaranth 0.1), and is now scheduled to be removed in version 0.5.

### Migrating from version 0.3

Apply the following changes to code written against Amaranth 0.3 to migrate it to version 0.4:

- Update shell environment to use `AMARANTH_*` environment variables instead of `NMIGEN_*` environment variables.
- Update shell environment to use `AMARANTH_ENV_<TOOLCHAIN>` (with all-uppercase `<TOOLCHAIN>` name) environment variable names instead of `AMARANTH_ENV_<Toolchain>` or `NMIGEN_ENV_<Toolchain>` (with mixed-case `<Toolchain>` name).
- Update imports of the form `from amaranth.vendor.some_vendor import SomeVendorPlatform` to `from amaranth.vendor import SomeVendorPlatform`. This change will reduce future churn.
- Replace uses of `Const.normalize(value, shape)` with `Const(value, shape).value`.
- Replace uses of `Repl(value, count)` with `value.replicate(count)`.
- Replace uses of `Record` with [`amaranth.lib.data`][amaranth.lib.data] and [`amaranth.lib.wiring`][amaranth.lib.wiring]. The appropriate replacement depends on the use case. If `Record` was being used for data storage and accessing the bit-level representation, use [`amaranth.lib.data`][amaranth.lib.data]. If `Record` was being used for connecting design components together, use [`amaranth.lib.wiring`][amaranth.lib.wiring].
- Replace uses of `Sample`, `Past`, `Stable`, `Rose`, `Fell` with a manually instantiated register, e.g. `past_x = Signal.like(x); m.d.sync += past_x.eq(x)`.
- Remove uses of `amaranth.compat` by migrating to native Amaranth syntax.
- Ensure the `Pin` instance returned by `platform.request` is not cast to value directly, but used for its fields. Replace code like `leds = Cat(platform.request(led, n) for n in range(4))` with `leds = Cat(platform.request(led, n).o for n in range(4))` (note the `.o`).
- Remove uses of `amaranth.lib.scheduler.RoundRobin` by inlining or copying the implementation of that class.
- Remove uses of `amaranth.lib.fifo.SyncFIFO(fwft=False)` and `amaranth.lib.fifo.FIFOInterface(fwft=False)` by converting code to use `fwft=True` FIFOs or copying the implementation of those classes.

While code that uses the features listed as deprecated below will work in Amaranth 0.4, they will be removed in the next version.

### Implemented RFCs

- [RFC 1]: Aggregate data structure library
- [RFC 2]: Interface definition library
- [RFC 3]: Enumeration shapes
- [RFC 4]: Constant-castable expressions
- [RFC 5]: Remove `Const.normalize`
- [RFC 6]: CRC generator
- [RFC 8]: Aggregate extensibility
- [RFC 9]: Constant initialization for shape-castable objects
- [RFC 10]: Move `Repl` to `Value.replicate`
- [RFC 18]: Reorganize vendor platforms
- [RFC 19]: Remove `amaranth.lib.scheduler`
- [RFC 15]: Lifting shape-castable objects
- [RFC 20]: Deprecate non-FWFT FIFOs
- [RFC 22]: Define `ValueCastable.shape()`
- [RFC 28]: Allow overriding `Value` operators
- [RFC 31]: Enumeration type safety
- [RFC 34]: Rename `amaranth.lib.wiring.Interface` to `PureInterface`
- [RFC 35]: Add `ShapeLike`, `ValueLike`
- [RFC 37]: Make `Signature` immutable
- [RFC 38]: `Component.signature` immutability

### Language changes

- Added: [`ShapeCastable`][amaranth.hdl.ShapeCastable], similar to [`ValueCastable`][amaranth.hdl.ValueCastable].
- Added: [`ShapeLike`][amaranth.hdl.ShapeLike] and [`ValueLike`][amaranth.hdl.ValueLike]. ([RFC 35])
- Added: [`Value.as_signed`][amaranth.hdl.Value.as_signed] and [`Value.as_unsigned`][amaranth.hdl.Value.as_unsigned] can be used on left-hand side of assignment (with no difference in behavior).
- Added: [`Const.cast`][amaranth.hdl.Const.cast]. ([RFC 4])
- Added: `Signal(reset=)`, [`Value.matches`][amaranth.hdl.Value.matches], `with m.Case():` accept any constant-castable objects. ([RFC 4])
- Added: [`Value.replicate`][amaranth.hdl.Value.replicate], superseding [`Repl`][amaranth.hdl.Repl]. ([RFC 10])
- Added: [`Memory`][amaranth.hdl.Memory] supports transparent read ports with read enable.
- Changed: creating a [`Signal`][amaranth.hdl.Signal] with a shape that is a [`ShapeCastable`][amaranth.hdl.ShapeCastable] implementing [`ShapeCastable.__call__`][amaranth.hdl.ShapeCastable.__call__] wraps the returned object using that method. ([RFC 15])
- Changed: [`Value.cast`][amaranth.hdl.Value.cast] casts [`ValueCastable`][amaranth.hdl.ValueCastable] objects recursively.
- Changed: [`Value.cast`][amaranth.hdl.Value.cast] treats instances of classes derived from both [`enum.Enum`][amaranth.hdl.enum.Enum] and [`int`][amaranth.hdl.int] (including [`enum.IntEnum`][amaranth.hdl.enum.IntEnum]) as enumerations rather than integers.
- Changed: [`Value.matches`][amaranth.hdl.Value.matches] with an empty list of patterns returns `Const(1)` rather than `Const(0)`, to match the behavior of `with m.Case():`.
- Changed: [`Cat`][Cat] warns if an enumeration without an explicitly specified shape is used. ([RFC 3])
- Changed: `signed(0)` is no longer constructible. (The semantics of this shape were never defined.)
- Changed: [`Value.__abs__`][amaranth.hdl.Value.__abs__] returns an unsigned value.
- Deprecated: [`ast.Sample`][amaranth.hdl.ast.Sample], [`ast.Past`][amaranth.hdl.ast.Past], [`ast.Stable`][amaranth.hdl.ast.Stable], [`ast.Rose`][amaranth.hdl.ast.Rose], [`ast.Fell`][amaranth.hdl.ast.Fell]. (Predating the RFC process.)
- Deprecated: [`Const.normalize`][amaranth.hdl.Const.normalize]; use `Const(value, shape).value` instead of `Const.normalize(value, shape)`. ([RFC 5])
- Deprecated: [`Repl`][amaranth.hdl.Repl]; use [`Value.replicate`][amaranth.hdl.Value.replicate] instead. ([RFC 10])
- Deprecated: [`Record`][amaranth.hdl.Record]; use [`amaranth.lib.data`][amaranth.lib.data] and [`amaranth.lib.wiring`][amaranth.lib.wiring] instead. ([RFC 1], [RFC 2])
- Removed: (deprecated in 0.1) casting of [`Shape`][amaranth.hdl.Shape] to and from a `(width, signed)` tuple.
- Removed: (deprecated in 0.3) [`ast.UserValue`][amaranth.hdl.ast.UserValue].
- Removed: (deprecated in 0.3) support for `# nmigen:` linter instructions at the beginning of file.

### Standard library changes

- Added: [`amaranth.lib.enum`][amaranth.lib.enum]. ([RFC 3])
- Added: [`amaranth.lib.data`][amaranth.lib.data]. ([RFC 1])
- Added: [`amaranth.lib.wiring`][amaranth.lib.wiring]. ([RFC 2])
- Added: [`amaranth.lib.crc`][amaranth.lib.crc]. ([RFC 6])
- Deprecated: [`amaranth.lib.scheduler`][amaranth.lib.scheduler]. ([RFC 19])
- Deprecated: [`amaranth.lib.fifo.FIFOInterface`][amaranth.lib.fifo.FIFOInterface] with `fwft=False`. ([RFC 20])
- Deprecated: [`amaranth.lib.fifo.SyncFIFO`][amaranth.lib.fifo.SyncFIFO] with `fwft=False`. ([RFC 20])

### Toolchain changes

- Changed: text files are written with LF line endings on Windows, like on other platforms.
- Added: `debug_verilog` override in [`build.TemplatedPlatform`][amaranth.build.TemplatedPlatform].
- Added: `env=` argument to [`build.run.BuildPlan.execute_local`][amaranth.build.run.BuildPlan.execute_local].
- Changed: [`build.run.BuildPlan.add_file`][amaranth.build.run.BuildPlan.add_file] rejects absolute paths.
- Deprecated: use of mixed-case toolchain environment variable names, such as `NMIGEN_ENV_Diamond` or `AMARANTH_ENV_Diamond`; use upper-case environment variable names, such as `AMARANTH_ENV_DIAMOND`.
- Removed: (deprecated in 0.3) [`sim.Simulator.step`][amaranth.sim.Simulator.step].
- Removed: (deprecated in 0.3) [`back.pysim`][back.pysim].
- Removed: (deprecated in 0.3) support for invoking [`back.rtlil.convert()`][back.rtlil.convert()] and [`back.verilog.convert()`][back.verilog.convert()] without an explicit `ports=` argument.
- Removed: (deprecated in 0.3) [`test`][test].

### Platform integration changes

- Added: `icepack_opts` override in [`vendor.LatticeICE40Platform`][amaranth.vendor.vendor.LatticeICE40Platform].
- Added: `OSCH` as `default_clk` clock source in [`vendor.LatticeMachXO2Platform`][amaranth.vendor.vendor.LatticeMachXO2Platform], [`vendor.LatticeMachXO3LPlatform`][amaranth.vendor.vendor.LatticeMachXO3LPlatform].
- Added: Xray toolchain support in [`vendor.XilinxPlatform`][amaranth.vendor.vendor.XilinxPlatform].
- Added: Artix UltraScale+ part support in [`vendor.XilinxPlatform`][amaranth.vendor.vendor.XilinxPlatform].
- Added: [`vendor.GowinPlatform`][amaranth.vendor.vendor.GowinPlatform].
- Deprecated: [`vendor.intel`][vendor.intel], [`vendor.lattice_ecp5`][vendor.lattice_ecp5], [`vendor.lattice_ice40`][vendor.lattice_ice40], [`vendor.lattice_machxo2_3l`][vendor.lattice_machxo2_3l], [`vendor.quicklogic`][vendor.quicklogic], [`vendor.xilinx`][vendor.xilinx]; import platforms directly from [`vendor`][vendor] instead. ([RFC 18])
- Removed: (deprecated in 0.3) [`lattice_machxo2`][lattice_machxo2]
- Removed: (deprecated in 0.3) [`lattice_machxo_2_3l.LatticeMachXO2Or3LPlatform`][amaranth.vendor.lattice_machxo_2_3l.LatticeMachXO2Or3LPlatform] SVF programming vector `{{name}}.svf`.
- Removed: (deprecated in 0.3) [`xilinx_spartan_3_6.XilinxSpartan3APlatform`][amaranth.vendor.xilinx_spartan_3_6.XilinxSpartan3APlatform], [`xilinx_spartan_3_6.XilinxSpartan6Platform`][amaranth.vendor.xilinx_spartan_3_6.XilinxSpartan6Platform], [`xilinx_7series.Xilinx7SeriesPlatform`][amaranth.vendor.xilinx_7series.Xilinx7SeriesPlatform], [`xilinx_ultrascale.XilinxUltrascalePlatform`][amaranth.vendor.xilinx_ultrascale.XilinxUltrascalePlatform].

## Version 0.3

The project has been renamed from nMigen to Amaranth.

Features deprecated in version 0.2 have been removed.

### Migrating from version 0.2

Apply the following changes to code written against nMigen 0.2 to migrate it to Amaranth 0.3:

- Update `import nmigen as nm` {ref}`explicit prelude imports <lang-prelude>` to be `import amaranth as am`, and adjust the code to use the `am.*` namespace.
- Update `import nmigen.*` imports to be `import amaranth.*`.
- Update `import nmigen_boards.*` imports to be `import amaranth_boards.*`.
- Update board definitions using [`vendor.lattice_machxo2.LatticeMachXO2Platform`][amaranth.vendor.lattice_machxo2.LatticeMachXO2Platform] to use [`vendor.lattice_machxo_2_3l.LatticeMachXO2Platform`][amaranth.vendor.lattice_machxo_2_3l.LatticeMachXO2Platform].
- Update board definitions using [`vendor.xilinx_spartan_3_6.XilinxSpartan3APlatform`][amaranth.vendor.xilinx_spartan_3_6.XilinxSpartan3APlatform], [`vendor.xilinx_spartan_3_6.XilinxSpartan6Platform`][amaranth.vendor.xilinx_spartan_3_6.XilinxSpartan6Platform], [`vendor.xilinx_7series.Xilinx7SeriesPlatform`][amaranth.vendor.xilinx_7series.Xilinx7SeriesPlatform], [`vendor.xilinx_ultrascale.XilinxUltrascalePlatform`][amaranth.vendor.xilinx_ultrascale.XilinxUltrascalePlatform] to use [`vendor.xilinx.XilinxPlatform`][amaranth.vendor.xilinx.XilinxPlatform].
- Switch uses of [`hdl.ast.UserValue`][amaranth.hdl.ast.UserValue] to [`ValueCastable`][amaranth.ValueCastable]; note that [`ValueCastable`][amaranth.ValueCastable] does not inherit from [`Value`][amaranth.Value], and inheriting from [`Value`][amaranth.Value] is not supported.
- Switch uses of [`back.pysim`][back.pysim] to [`sim`][sim].
- Add an explicit `ports=` argument to uses of [`back.rtlil.convert`][back.rtlil.convert] and [`back.verilog.convert`][back.verilog.convert] if missing.
- Remove uses of [`test.utils.FHDLTestCase`][amaranth.test.utils.FHDLTestCase] and vendor the implementation of [`test.utils.FHDLTestCase.assertFormal`][amaranth.test.utils.FHDLTestCase.assertFormal] if necessary.

While code that uses the features listed as deprecated below will work in Amaranth 0.3, they will be removed in the next version.

### Language changes

- Added: [`Value`][amaranth.hdl.Value] can be used with [`abs`][abs].
- Added: [`Value.rotate_left`][amaranth.hdl.Value.rotate_left] and [`Value.rotate_right`][amaranth.hdl.Value.rotate_right].
- Added: [`Value.shift_left`][amaranth.hdl.Value.shift_left] and [`Value.shift_right`][amaranth.hdl.Value.shift_right].
- Added: [`ValueCastable`][amaranth.hdl.ValueCastable].
- Deprecated: [`ast.UserValue`][amaranth.hdl.ast.UserValue]; use [`ValueCastable`][amaranth.hdl.ValueCastable] instead.
- Added: Division and modulo operators can be used with a negative divisor.
- Deprecated: `# nmigen:` linter instructions at the beginning of file; use `# amaranth:` instead.

### Standard library changes

- Added: [`cdc.PulseSynchronizer`][amaranth.lib.cdc.PulseSynchronizer].
- Added: [`cdc.AsyncFFSynchronizer`][amaranth.lib.cdc.AsyncFFSynchronizer].
- Changed: [`fifo.AsyncFIFO`][amaranth.lib.fifo.AsyncFIFO] is reset when the write domain is reset.
- Added: [`fifo.AsyncFIFO.r_rst`][amaranth.lib.fifo.AsyncFIFO.r_rst] is asserted when the write domain is reset.
- Added: [`fifo.FIFOInterface.r_level`][amaranth.lib.fifo.FIFOInterface.r_level] and [`fifo.FIFOInterface.w_level`][amaranth.lib.fifo.FIFOInterface.w_level].

### Toolchain changes

- Changed: Backend and simulator reject wires larger than 65536 bits.
- Added: Backend emits Yosys enumeration attributes for {ref}`enumeration-shaped <lang-shapeenum>` signals.
- Added: If a compatible Yosys version is not installed, [`back.verilog`][back.verilog] will fall back to the [amaranth-yosys](https://github.com/amaranth-lang/amaranth-yosys) PyPI package. The package can be {ref}`installed <install>` as `amaranth[builtin-yosys]` to ensure this dependency is available.
- Added: [`back.cxxrtl`][back.cxxrtl].
- Added: [`sim`][sim], a simulator interface with support for multiple simulation backends.
- Deprecated: [`back.pysim`][back.pysim]; use [`sim`][sim] instead.
- Removed: The `with Simulator(fragment, ...) as sim:` form.
- Removed: [`sim.Simulator.add_process`][amaranth.sim.Simulator.add_process] with a generator argument.
- Deprecated: [`sim.Simulator.step`][amaranth.sim.Simulator.step]; use [`sim.Simulator.advance`][amaranth.sim.Simulator.advance] instead.
- Added: [`build.BuildPlan.execute_remote_ssh`][amaranth.build.BuildPlan.execute_remote_ssh].
- Deprecated: [`test.utils.FHDLTestCase`][amaranth.test.utils.FHDLTestCase], with no replacement.
- Deprecated: [`back.rtlil.convert()`][back.rtlil.convert()] and [`back.verilog.convert()`][back.verilog.convert()] without an explicit `ports=` argument.
- Changed: VCD output now uses a top-level "bench" module that contains testbench only signals.
- Deprecated: `NMIGEN_*` environment variables; use `AMARANTH_*` environment variables instead.

### Platform integration changes

- Added: `SB_LFOSC` and `SB_HFOSC` as `default_clk` clock sources in [`lattice_ice40.LatticeICE40Platform`][amaranth.vendor.lattice_ice40.LatticeICE40Platform].
- Added: [`lattice_machxo2.LatticeMachXO2Platform`][amaranth.vendor.lattice_machxo2.LatticeMachXO2Platform] generates binary (`.bit`) bitstreams.
- Added: [`lattice_machxo_2_3l.LatticeMachXO3LPlatform`][amaranth.vendor.lattice_machxo_2_3l.LatticeMachXO3LPlatform].
- Deprecated: [`lattice_machxo2`][lattice_machxo2]; use [`lattice_machxo_2_3l.LatticeMachXO2Platform`][amaranth.vendor.lattice_machxo_2_3l.LatticeMachXO2Platform] instead.
- Removed: [`xilinx_7series.Xilinx7SeriesPlatform.grade`][amaranth.vendor.xilinx_7series.Xilinx7SeriesPlatform.grade]; this family has no temperature grades.
- Removed: [`xilinx_ultrascale.XilinxUltrascalePlatform.grade`][amaranth.vendor.xilinx_ultrascale.XilinxUltrascalePlatform.grade]; this family has temperature grade as part of speed grade.
- Added: Symbiflow toolchain support for [`xilinx_7series.Xilinx7SeriesPlatform`][amaranth.vendor.xilinx_7series.Xilinx7SeriesPlatform].
- Added: [`lattice_machxo_2_3l.LatticeMachXO2Or3LPlatform`][amaranth.vendor.lattice_machxo_2_3l.LatticeMachXO2Or3LPlatform] generates separate Flash and SRAM SVF programming vectors, `{{name}}_flash.svf` and `{{name}}_sram.svf`.
- Deprecated: [`lattice_machxo_2_3l.LatticeMachXO2Or3LPlatform`][amaranth.vendor.lattice_machxo_2_3l.LatticeMachXO2Or3LPlatform] SVF programming vector `{{name}}.svf`; use `{{name}}_flash.svf` instead.
- Added: [`quicklogic.QuicklogicPlatform`][amaranth.vendor.quicklogic.QuicklogicPlatform].
- Added: `cyclonev_oscillator` as `default_clk` clock source in [`intel.IntelPlatform`][amaranth.vendor.intel.IntelPlatform].
- Added: `add_settings` and `add_constraints` overrides in [`intel.IntelPlatform`][amaranth.vendor.intel.IntelPlatform].
- Added: [`xilinx.XilinxPlatform`][amaranth.vendor.xilinx.XilinxPlatform].
- Deprecated: [`xilinx_spartan_3_6.XilinxSpartan3APlatform`][amaranth.vendor.xilinx_spartan_3_6.XilinxSpartan3APlatform], [`xilinx_spartan_3_6.XilinxSpartan6Platform`][amaranth.vendor.xilinx_spartan_3_6.XilinxSpartan6Platform], [`xilinx_7series.Xilinx7SeriesPlatform`][amaranth.vendor.xilinx_7series.Xilinx7SeriesPlatform], [`xilinx_ultrascale.XilinxUltrascalePlatform`][amaranth.vendor.xilinx_ultrascale.XilinxUltrascalePlatform]; use [`xilinx.XilinxPlatform`][amaranth.vendor.xilinx.XilinxPlatform] instead.
- Added: Mistral toolchain support for [`intel.IntelPlatform`][amaranth.vendor.intel.IntelPlatform].
- Added: `synth_design_opts` override in [`xilinx.XilinxPlatform`][amaranth.vendor.xilinx.XilinxPlatform].

## Versions 0.1, 0.2

No changelog is provided for these versions.

The PyPI packages were published under the `nmigen` namespace, rather than `amaranth`.

[rfc 1]: https://amaranth-lang.org/rfcs/0001-aggregate-data-structures.html
[rfc 10]: https://amaranth-lang.org/rfcs/0010-move-repl-to-value.html
[rfc 15]: https://amaranth-lang.org/rfcs/0015-lifting-shape-castables.html
[rfc 17]: https://amaranth-lang.org/rfcs/0017-remove-log2-int.html
[rfc 18]: https://amaranth-lang.org/rfcs/0018-reorganize-vendor-platforms.html
[rfc 19]: https://amaranth-lang.org/rfcs/0019-remove-scheduler.html
[rfc 2]: https://amaranth-lang.org/rfcs/0002-interfaces.html
[rfc 20]: https://amaranth-lang.org/rfcs/0020-deprecate-non-fwft-fifos.html
[rfc 22]: https://amaranth-lang.org/rfcs/0022-valuecastable-shape.html
[rfc 27]: https://amaranth-lang.org/rfcs/0027-simulator-testbenches.html
[rfc 28]: https://amaranth-lang.org/rfcs/0028-override-value-operators.html
[rfc 3]: https://amaranth-lang.org/rfcs/0003-enumeration-shapes.html
[rfc 30]: https://amaranth-lang.org/rfcs/0030-component-metadata.html
[rfc 31]: https://amaranth-lang.org/rfcs/0031-enumeration-type-safety.html
[rfc 34]: https://amaranth-lang.org/rfcs/0034-interface-rename.html
[rfc 35]: https://amaranth-lang.org/rfcs/0035-shapelike-valuelike.html
[rfc 36]: https://amaranth-lang.org/rfcs/0036-async-testbench-functions.html
[rfc 37]: https://amaranth-lang.org/rfcs/0037-make-signature-immutable.html
[rfc 38]: https://amaranth-lang.org/rfcs/0038-component-signature-immutability.html
[rfc 39]: https://amaranth-lang.org/rfcs/0039-empty-case.html
[rfc 4]: https://amaranth-lang.org/rfcs/0004-const-castable-exprs.html
[rfc 42]: https://amaranth-lang.org/rfcs/0042-const-from-shape-castable.html
[rfc 43]: https://amaranth-lang.org/rfcs/0043-rename-reset-to-init.html
[rfc 45]: https://amaranth-lang.org/rfcs/0045-lib-memory.html
[rfc 46]: https://amaranth-lang.org/rfcs/0046-shape-range-1.html
[rfc 5]: https://amaranth-lang.org/rfcs/0005-remove-const-normalize.html
[rfc 50]: https://amaranth-lang.org/rfcs/0050-print.html
[rfc 51]: https://amaranth-lang.org/rfcs/0051-const-from-bits.html
[rfc 53]: https://amaranth-lang.org/rfcs/0053-ioport.html
[rfc 55]: https://amaranth-lang.org/rfcs/0055-lib-io.html
[rfc 58]: https://amaranth-lang.org/rfcs/0058-valuecastable-format.html
[rfc 59]: https://amaranth-lang.org/rfcs/0059-no-domain-upwards-propagation.html
[rfc 6]: https://amaranth-lang.org/rfcs/0006-stdlib-crc.html
[rfc 61]: https://amaranth-lang.org/rfcs/0061-minimal-streams.html
[rfc 62]: https://amaranth-lang.org/rfcs/0062-memory-data.html
[rfc 63]: https://amaranth-lang.org/rfcs/0063-remove-lib-coding.html
[rfc 65]: https://amaranth-lang.org/rfcs/0065-format-struct-enum.html
[rfc 66]: https://amaranth-lang.org/rfcs/0066-simulation-time.html
[rfc 69]: https://amaranth-lang.org/rfcs/0069-simulation-port.html
[rfc 71]: https://amaranth-lang.org/rfcs/0071-enumview-matches.html
[rfc 8]: https://amaranth-lang.org/rfcs/0008-aggregate-extensibility.html
[rfc 9]: https://amaranth-lang.org/rfcs/0009-const-init-shape-castable.html
