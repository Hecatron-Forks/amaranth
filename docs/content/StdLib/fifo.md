# First-in first-out queues

```{eval-rst}
.. py:module:: amaranth.lib.fifo
```

The `amaranth.lib.fifo` module provides building blocks for first-in, first-out queues.

```{eval-rst}
.. autoclass:: FIFOInterface

   .. note::

      The :class:`FIFOInterface` class can be used directly to substitute a FIFO in tests, or inherited from in a custom FIFO implementation.
```

```{eval-rst}
.. autoclass:: SyncFIFO(*, width, depth)
```

```{eval-rst}
.. autoclass:: SyncFIFOBuffered(*, width, depth)
```

```{eval-rst}
.. autoclass:: AsyncFIFO(*, width, depth, r_domain="read", w_domain="write", exact_depth=False)
```

```{eval-rst}
.. autoclass:: AsyncFIFOBuffered(*, width, depth, r_domain="read", w_domain="write", exact_depth=False)
```
