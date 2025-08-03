const mongoose = require('mongoose');

// Define shared schema fields
const schemaFields = {
  BALANCE: Number,
  BALANCE_FREQUENCY: Number,
  PURCHASES: Number,
  ONEOFF_PURCHASES: Number,
  INSTALLMENTS_PURCHASES: Number,
  CASH_ADVANCE: Number,
  PURCHASES_FREQUENCY: Number,
  ONEOFF_PURCHASES_FREQUENCY: Number,
  PURCHASES_INSTALLMENTS_FREQUENCY: Number,
  CASH_ADVANCE_FREQUENCY: Number,
  CASH_ADVANCE_TRX: Number,
  PURCHASES_TRX: Number,
  CREDIT_LIMIT: Number,
  PAYMENTS: Number,
  MINIMUM_PAYMENTS: Number,
  PRC_FULL_PAYMENT: Number,
  TENURE: Number
};

// Reuse schema fields for both segment and predict schemas
const SegmentSchema = new mongoose.Schema(schemaFields);
const PredictSchema = new mongoose.Schema(schemaFields);

// Create models
const Segment = mongoose.model('Segment', SegmentSchema);
const Predict = mongoose.model('Predict', PredictSchema);

// Export both
module.exports = { Segment, Predict };
