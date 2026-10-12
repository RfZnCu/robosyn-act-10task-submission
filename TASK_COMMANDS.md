# Ten task commands and immutable checkpoint mappings

All tasks use the corrected immutable GitHub source revision produced from this
repository. Each task uses its own final ACT_SEU_MAI checkpoint revision below.

| Task | Immutable checkpoint URL |
|---|---|
| `table_rearrangement` | https://huggingface.co/RfZnCu/robosyn-act-table-rearrangement/tree/a1714858b2a0f60caa12827f26e5fc540611a5dc |
| `click_bell` | https://huggingface.co/RfZnCu/robosyn-act-click-bell/tree/1f7534dcb0874ce8bcd5b359e622a8b2d5cfe4af |
| `water_pouring` | https://huggingface.co/RfZnCu/robosyn-act-water-pouring/tree/316fd087140c5c44d0eac382f9b3ffc1be2cca67 |
| `handle_basket` | https://huggingface.co/RfZnCu/robosyn-act-handle-basket/tree/72175ef1cc5cd0d88be0022db524b7ad4fafa22c |
| `items_handover` | https://huggingface.co/RfZnCu/robosyn-act-items-handover/tree/38e3b524d2719d8d380575499c8b64d5fae5a888 |
| `drawer_open_place` | https://huggingface.co/RfZnCu/robosyn-act-drawer-open-place/tree/b431185dc764337effd38c48a46cfdb6f7bec7f7 |
| `mixer_operating` | https://huggingface.co/RfZnCu/robosyn-act-mixer-operating/tree/d91fa73155a73382e8ca17ced0141347c32e2cb5 |
| `item_assembly` | https://huggingface.co/RfZnCu/robosyn-act-item-assembly/tree/010f170d6905c7a22cdfee084f684bede8dd2407 |
| `manipulate_pipette` | https://huggingface.co/RfZnCu/robosyn-act-manipulate-pipette/tree/4eaa1226bc9ba65850e78c105a11e1aa8a24a2cf |
| `sample_loading` | https://huggingface.co/RfZnCu/robosyn-act-sample-loading/tree/40077ea8a6c6ad826070647c7ebe80c0ddb7a452 |

## Commands

```bash
bash policy/act/eval.sh table_rearrangement random auto 0 --headless True
bash policy/act/eval.sh click_bell random auto 0 --headless True
bash policy/act/eval.sh water_pouring random auto 0 --headless True
bash policy/act/eval.sh handle_basket random auto 0 --headless True
bash policy/act/eval.sh items_handover random auto 0 --headless True
bash policy/act/eval.sh drawer_open_place random auto 0 --headless True
bash policy/act/eval.sh mixer_operating random auto 0 --headless True
bash policy/act/eval.sh item_assembly random auto 0 --headless True
bash policy/act/eval.sh manipulate_pipette random auto 0 --headless True
bash policy/act/eval.sh sample_loading random auto 0 --headless True
```

Replace GPU `0`, seed, and episode count only as assigned by the organizers. A
local checkpoint directory may replace `auto` when it contains the two required
files and corresponds to the listed immutable revision.
