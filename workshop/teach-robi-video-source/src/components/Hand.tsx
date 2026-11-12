import React from "react";

type Props = {
  skin: string;
  sleeve: string;
  down?: boolean;
  left?: boolean;
  size?: number;
  style?: React.CSSProperties;
};

const shade = (hex: string, amt: number) => {
  const n = parseInt(hex.slice(1), 16);
  const f = (v: number) => Math.max(0, Math.min(255, Math.round(v * (1 - amt))));
  const r = f(n >> 16);
  const g = f((n >> 8) & 255);
  const b = f(n & 255);
  return `rgb(${r},${g},${b})`;
};

const tint = (hex: string, amt: number) => {
  const n = parseInt(hex.slice(1), 16);
  const f = (v: number) => Math.round(v + (255 - v) * amt);
  return `rgb(${f(n >> 16)},${f((n >> 8) & 255)},${f(n & 255)})`;
};

/** A simple, original cartoon thumbs-up hand. `down` turns it into a thumbs down; `left` mirrors it. */
export const Hand: React.FC<Props> = ({ skin, sleeve, down = false, left = false, size = 200, style }) => {
  const line = shade(skin, 0.38);
  const sw = 6;
  return (
    <svg viewBox="0 0 200 260" width={size} height={size * 1.3} style={style}>
      <g transform={down ? "rotate(180 100 130)" : undefined}>
        <g transform={left ? "translate(200 0) scale(-1 1)" : undefined}>
          {/* sleeve */}
          <rect x={56} y={200} width={96} height={56} rx={12} fill={sleeve} />
          <rect x={56} y={200} width={96} height={12} rx={6} fill={shade(sleeve, 0.2)} />
          {/* fist */}
          <rect x={48} y={92} width={112} height={122} rx={34} fill={skin} stroke={line} strokeWidth={sw} />
          {/* curled fingers */}
          {[0, 1, 2, 3].map((i) => (
            <rect
              key={i}
              x={110}
              y={98 + i * 28}
              width={62}
              height={30}
              rx={15}
              fill={skin}
              stroke={line}
              strokeWidth={sw}
            />
          ))}
          {/* thumb */}
          <rect x={50} y={14} width={46} height={116} rx={23} fill={skin} stroke={line} strokeWidth={sw} />
          <rect x={59} y={23} width={28} height={22} rx={10} fill={tint(skin, 0.45)} />
        </g>
      </g>
    </svg>
  );
};
