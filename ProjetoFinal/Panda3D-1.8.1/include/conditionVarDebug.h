// Filename: conditionVarDebug.h
// Created by:  drose (13Feb06)
//
////////////////////////////////////////////////////////////////////
//
// PANDA 3D SOFTWARE
// Copyright (c) Carnegie Mellon University.  All rights reserved.
//
// All use of this software is subject to the terms of the revised BSD
// license.  You should have received a copy of this license along
// with this source code in a file named "LICENSE."
//
////////////////////////////////////////////////////////////////////

#ifndef CONDITIONVARDEBUG_H
#define CONDITIONVARDEBUG_H

#include "pandabase.h"
#include "pmutex.h"
#include "conditionVarImpl.h"

#ifdef DEBUG_THREADS

////////////////////////////////////////////////////////////////////
//       Class : ConditionVarDebug
// Description : A condition variable, usually used to communicate
//               information about changing state to a thread that is
//               waiting for something to happen.  A condition
//               variable can be used to "wake up" a thread when some
//               arbitrary condition has changed.
//
//               A condition variable is associated with a single
//               mutex, and several condition variables may share the
//               same mutex.
////////////////////////////////////////////////////////////////////
class EXPCL_PANDA_PIPELINE ConditionVarDebug {
public:
  ConditionVarDebug(MutexDebug &mutex);
  virtual ~ConditionVarDebug();
private:
  INLINE ConditionVarDebug(const ConditionVarDebug &copy);
  INLINE void operator = (const ConditionVarDebug &copy);

PUBLISHED:
  INLINE MutexDebug &get_mutex() const;

  BLOCKING void wait();
  BLOCKING void wait(double timeout);
  void notify();
  virtual void output(ostream &out) const;

private:
  MutexDebug &_mutex;
  ConditionVarImpl _impl;
};

INLINE ostream &
operator << (ostream &out, const ConditionVarDebug &cv) {
  cv.output(out);
  return out;
}

#include "conditionVarDebug.I"

#endif  // DEBUG_THREADS

#endif
