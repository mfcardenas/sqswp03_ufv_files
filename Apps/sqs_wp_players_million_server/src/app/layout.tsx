import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "ISOmillonario — Servidor de Persistencia",
  description: "Servidor de persistencia para el juego Quien quiere ser ISOmillonario",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es">
      <body>{children}</body>
    </html>
  );
}
