# Components

### Bracket Connector Line
**Role:** Structural diagram edge

1px hairline in #f2f2f2 connecting match nodes across the bracket. Turns to Bracket Pink (#f50db4) on the winning path. No curves - orthogonal right-angle joins only, like a circuit diagram.

### Winner Node (Pink Filled Box)
**Role:** Highlighted match result box

Filled #f50db4 square, 0px radius, white monospace text at 12px weight 500-700. Contains score number, team icon, or single-letter marker. Typically 24x24px or 32x32px. The pink fill = this is the advancing team.

### Team Identity Box (Black Filled)
**Role:** Team name or avatar container

Filled #000000 square, 0px radius, white text or white icon glyph. Adjacent to a white box with the score in black. The black/white pairing creates the scoreboard unit.

### Stage Label Tag (R16 / QF / SF)
**Role:** Round-of-tournament marker

Filled Bracket Pink (#f50db4) rectangle, 0px radius, white monospace text at 12px weight 500. Labels: R16, QF, SF, F. Positioned at the top of each bracket column.

### Status Pill (WINNER / Final / Road to final)
**Role:** Match-state annotation

Small uppercase text label. 'WINNER' sits as a Bracket Pink filled tag above the champion's node. 'Final' uses larger monospace at 32px weight 700 in Bracket Pink. 'Road to final' is centered body text in #000000.

### Central VS Separator
**Role:** Final-match divider

Large monospace 'VS' at ~40-56px weight 700 in Bracket Pink (#f50db4), centered between the two finalist teams. The typographic climax of the bracket.

### Header Nav Tags (GROUP STAGE / LIVESTREAM)
**Role:** Top navigation chips

Inverted style: black text on light gray (#f2f2f2) pill/rectangle tags with hairline borders, monospace 12px. Uniswap unicorn logo in Bracket Pink at the far left.

### Uniswap Cup Wordmark
**Role:** Page title lockup

'UNISWAP' in monospace 12px weight 500, dot separator, 'CUP' below in monospace with letter-spacing. Black on white, centered. No logo mark - type IS the mark.

### Tournament Bracket Frame
**Role:** Full-page layout container

Full-bleed white (#ffffff) canvas with bracket diagram spanning the full viewport width. A faint circle (the 'pitch') sits behind the final match at center. No card containers - nodes are directly placed on the canvas with hairline connectors.

### Match Date/Time Label
**Role:** Scheduling annotation

Monospace 12px text showing date and time (e.g., 'November 10' with '1pm' underlined). Black text on white, minimal, positioned beneath the central final match.
