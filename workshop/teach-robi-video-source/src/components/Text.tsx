import React from "react";
import { C, FONT } from "../theme";

export const Headline: React.FC<{ children: React.ReactNode; size?: number; color?: string; style?: React.CSSProperties }> = ({
  children,
  size = 104,
  color = C.ink,
  style,
}) => (
  <div style={{ fontFamily: FONT, fontWeight: 900, fontSize: size, lineHeight: 1.1, color, ...style }}>{children}</div>
);

export const Sub: React.FC<{ children: React.ReactNode; size?: number; color?: string; style?: React.CSSProperties }> = ({
  children,
  size = 64,
  color = C.muted,
  style,
}) => (
  <div style={{ fontFamily: FONT, fontWeight: 800, fontSize: size, lineHeight: 1.2, color, ...style }}>{children}</div>
);

export const Chip: React.FC<{ n: number; label: string; color: string; style?: React.CSSProperties }> = ({ n, label, color, style }) => (
  <div
    style={{
      display: "inline-flex",
      alignItems: "center",
      gap: 18,
      background: color,
      color: C.white,
      fontFamily: FONT,
      fontWeight: 900,
      fontSize: 52,
      padding: "14px 34px",
      borderRadius: 999,
      ...style,
    }}
  >
    <span
      style={{
        width: 64,
        height: 64,
        borderRadius: 999,
        background: C.white,
        color,
        display: "inline-flex",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      {n}
    </span>
    {label}
  </div>
);
