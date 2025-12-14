import bcrypt from 'bcryptjs';

export async function verifyPassword(password: string): Promise<boolean> {
  const hashedPassword = process.env.ADMIN_PASSWORD_HASH;
  
  if (!hashedPassword) {
    // For development only - allow 'admin123' as default password
    if (process.env.NODE_ENV !== 'production') {
      const defaultHash = await bcrypt.hash('admin123', 10);
      return bcrypt.compare(password, defaultHash);
    }
    throw new Error('ADMIN_PASSWORD_HASH must be set in production');
  }
  
  return bcrypt.compare(password, hashedPassword);
}

export async function hashPassword(password: string): Promise<string> {
  return bcrypt.hash(password, 10);
}
